from abc import ABC, abstractmethod

class FootballPerson(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role_info(self):
        pass
