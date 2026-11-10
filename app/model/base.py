from abc import ABC, abstractmethod
from typing import AsyncIterable

from app.models import Prompt

class Base(ABC):
    @abstractmethod
    def generate(self, prompt: Prompt) -> AsyncIterable[str]:
        ...