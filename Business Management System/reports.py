from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def render(self):
        pass

class CSVReport(Report):
    def __init__(self, data):
        self.data = data

    def render(self):
        return "\n".join([f"{d.client}, {d.total()}" for d in self.data])

class JSONReport(Report):
    def __init__(self, data):
        self.data = data

    def render(self):
        return str([{"client": d.client, "total": d.total()} for d in self.data])

class ReportFactory:
    @staticmethod
    def create(report_type, data):
        if report_type == "csv":
            return CSVReport(data)
        elif report_type == "json":
            return JSONReport(data)
        else:
            raise ValueError("Unknown report type")