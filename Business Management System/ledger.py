class Ledger:
    def __init__(self):
        self.entries = []

    def add_entry(self, document):
        self.entries.append(document)

    def total(self):
        return sum(doc.total() for doc in self.entries if hasattr(doc, 'total'))