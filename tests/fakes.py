from typing import AsyncIterable, Callable
from app.model.base import Base
from app.schemas import Prompt


def get_test_model():
    return StubModel()

class StubModel(Base):
    async def generate(self, prompt: Prompt) -> AsyncIterable[str]:
        yield prompt.prompt
        for _ in range(prompt.max_tokens):
            yield "test"

class GenerateRequestSpy():
    calls: list

    def __init__(self):
        self.calls = []

    def __call__(self, prompt) -> None:
        self.calls.append(prompt)