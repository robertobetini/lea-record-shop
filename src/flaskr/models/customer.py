from datetime import date

class Customer:
    def __init__(self, document: str, name: str, birth_date: date, email: str, phone: str):
        self.document = document
        self.name = name
        self.birth_date = birth_date
        self.email = email
        self.phone = phone
        self.active = True
        