from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def render(self):
        pass

class Invoice(Document):
    def __init__(self, client, items):
        self.client = client
        self.items = items  # list of tuples (description, amount)

    def total(self):
        return sum(amount for _, amount in self.items)

    def render(self):
        lines = [f"Invoice for {self.client}", "-------------------"]
        for desc, amt in self.items:
            lines.append(f"{desc}: ${amt}")
        lines.append(f"Total: ${self.total()}")
        return '\n'.join(lines)