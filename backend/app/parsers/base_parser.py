from abc import ABC
from abc import abstractmethod


class BaseParser(ABC):

    @abstractmethod
    def parse(self, text: str):
        pass