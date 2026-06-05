from dataclasses import dataclass

@dataclass
class Person:
    last_name: str
    first_name: str
    due: str

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_due(self) -> float:
        return float(self.due.replace("$", ""))
    