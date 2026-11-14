from collections.abc import AsyncIterable

from app.model.base import Base
from app.schemas import Prompt


def get_test_model():
    return StubModel()


def get_no_yield_model():
    return NoYieldModel()


class StubModel(Base):
    async def generate(self, prompt: Prompt) -> AsyncIterable[str]:
        for _ in range(prompt.max_tokens):
            yield "test"


class NoYieldModel(Base):
    async def generate(self, prompt: Prompt) -> AsyncIterable[str]:
        for _ in range(0):
            yield "test"


class GenerateRequestSpy:
    calls: list

    def __init__(self):
        self.calls = []

    def __call__(
        self,
        prompt: Prompt,
        ttft: float | None,
        total_gen_time: float,
        output_token_count: int,
    ) -> None:
        self.calls.append([prompt, ttft, total_gen_time, output_token_count])
