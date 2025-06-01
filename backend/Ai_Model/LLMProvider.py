import json
from abc import ABC, abstractmethod
from typing import List

"""


"""


class LlmProvider(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def clean(self, text: str) -> str:
        pass

    @abstractmethod
    def add_instructions(self, instructions: List[str], prompt: json) -> json:
        pass

    @abstractmethod
    def add_query(self, query: str, prompt: json) -> json:
        pass
