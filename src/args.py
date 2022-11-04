from dataclasses import dataclass, field
from typing import Optional
from argparse_dataclass import ArgumentParser

@dataclass 
class Args:
    api_key: str
    company_name: str
    mail_from: str = field(metadata=dict(args=["--from"]))
    signature: str = field(default="Some Anonymous Asshole")
    debug: bool = field(default=False, metadata=dict(args=["-d", "--debug"]))
    dry_run: bool = field(default=False)
    smtp_host: str = field(default="localhost")
    smtp_port: str = field(default=25)
    smtp_tls: bool = field(default=False)
    smtp_username: Optional[str] = field(default=None)
    smtp_password: Optional[str] = field(default=None)

@staticmethod
def parse(args: list[str]) -> Args:
    parser = ArgumentParser(Args,
        description='An automated executive email carpet bomber. The worst tool you never knew you needed to channel your inner Karen.'
    )
    return parser.parse_args()