from dataclasses import dataclass

@dataclass
class Company:
    id: str
    name: str
    domain: str

    def __repr__(self) -> str:
        return f'{self.name} ({self.domain}; {self.id})'
