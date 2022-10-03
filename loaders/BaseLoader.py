from Contact import Contact
from abc import ABC, abstractmethod


class BaseLoader(ABC):

    @abstractmethod
    def load_contacts(self) -> [Contact]:
        pass

    @abstractmethod
    def save_contacts(self, contacts: [Contact]):
        pass

