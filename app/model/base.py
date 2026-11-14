from abc import ABC, abstractmethod
from collections.abc import AsyncIterable

from app.schemas import Prompt


class Base(ABC):
    @abstractmethod
    def generate(self, prompt: Prompt) -> AsyncIterable[str]: ...
