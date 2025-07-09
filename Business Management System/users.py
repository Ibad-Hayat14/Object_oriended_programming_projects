from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email):
        self.name = name
        self._email = email

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return f"{self.name} ({self.role()})"

class Admin(User):
    def role(self):
        return "Admin"

class Employee(User):
    def role(self):
        return "Employee"

class Customer(User):
    def role(self):
        return "Customer"