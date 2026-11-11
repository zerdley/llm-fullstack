import asyncio
import random
from typing import AsyncIterable
from app.model.base import Base
from app.schemas import Prompt

class FakeModel(Base):
    async def generate(self, prompt: Prompt) -> AsyncIterable[str]:
        with open("/usr/share/dict/words", "r", encoding='utf-8') as f:
            word_list = [word.strip() for word in f if word.strip().isalpha()]

        yield prompt.prompt + "\n"
        for _ in range(prompt.max_tokens):
            await asyncio.sleep(0.05)
            yield random.choice(word_list) + " "