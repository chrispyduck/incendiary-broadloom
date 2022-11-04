import requests
import urllib.parse
from htmldom import htmldom
from bs4 import BeautifulSoup

def generate_complaint(company_name: str) -> str:
    raw = requests.get("https://www.pakin.org/complaint", {
        'firstname': company_name,
        'paragraphs': 3,
        'gender': 'c',
        'shorttype': 'f'
    }, cookies={
        'ACLG_agreed': 'yeah'
    }).content

    return "\n\n".join([item.text for item in BeautifulSoup(raw, "lxml").find_all("p")])
