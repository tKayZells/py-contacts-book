import csv

from BaseLoader import BaseLoader
from Contact import Contact


class FileLoader(BaseLoader):

    def __init__(self, file_name: str):
        self._file_name = file_name

    def load_contacts(self) -> [Contact]:
        contacts: [Contact] = []
        with open(self._file_name, "r", encoding="utf8") as contact_book:
            reader = csv.DictReader(contact_book, Contact.field_columns)
            for row in reader:
                contacts.append(
                    Contact(
                        row['name'],
                        row['last_name'],
                        row['email'],
                        row['phone']
                    )
                )
        return contacts

    def save_contacts(self, contacts: [Contact]):
        raise NotImplementedError()

