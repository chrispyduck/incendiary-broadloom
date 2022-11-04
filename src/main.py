from time import sleep
import logging
import peopledatalabs
from typing import Optional
from pydantic import BaseModel
from sys import argv 
import smtplib 
import ssl
from .contact import Contact
from .args import parse as parse_args
from .company import Company
from .complaint import generate_complaint

args = parse_args(argv)

if args.debug:
    import http.client as http_client
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

pdl = peopledatalabs.PDLPY(
    api_key=args.api_key,
)

# fetches a company ID from a name
def get_company_id(name: str) -> Company:
    # get company id
    result = pdl.company.enrichment(
        name=name
    )

    result_json = result.json()
    if result.ok:
        return Company(result_json['id'], result_json['name'], result_json['website'])

    message = result_json['error']['message']
    raise Exception(
        f'Unable to match company "{name}" to ID: {result.reason}: {message}')

# given a company id, fetch a list of executives
def get_executive_contacts_for_company(company: Company) -> list[Contact]:
    result = pdl.person.search(
        query={
            'query': {
                'bool': {
                    'must': [
                        {'term': {'job_company_id': company.id}},
                        {'term': {'job_title_levels': 'cxo'}},
                    ]
                }
            }
        },
        size=25,
        titlecase=True)

    result_json = result.json()
    if result.ok:
        return [Contact(match['full_name'], match['work_email'], match['job_title']) for match in result_json['data']]

    message = result_json['error']['message']
    raise Exception(
        f'Error identifying company executives: {result.reason}: {message}')

def generate_mail_body(contact: Contact, complaint: str, signature: str) -> str:
    return f"""Dear {contact.name},
            
{complaint}

Sincerely,

{signature}

"""

def main():
    company_id = get_company_id(args.company_name)
    execs = get_executive_contacts_for_company(company_id)
    
    print(f"Found {len(execs)} executives:")
    for contact in execs:
        print(contact)
    
    complaint = generate_complaint(args.company_name)

    if args.dry_run:
        print(f'** WARNING ** Dry run. Printing first email to stdout and exiting.')
        print(generate_mail_body(execs[0], complaint, args.signature))
        return

    with smtplib.SMTP_SSL(args.smtp_host, args.smtp_port, context=ssl.create_default_context()) if args.smtp_tls else smtplib.SMTP(args.smtp_host, args.smtp_port) as server:
        if args.smtp_username and args.smtp_password:
            server.login(args.smtp_username, args.smtp_password)
        for exec in execs:
            if exec.email:
                print(f'Sending email to {exec.name} at {exec.email}')
                message = generate_mail_body(exec, complaint, args.signature)
                server.sendmail(args.mail_from, exec.email, message)

