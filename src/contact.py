from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    email: str
    position: str 
    
    def __repr__(self):
        return f"{self.name} <{self.email}> ({self.position})"