import random
from typing import AsyncIterable

from app.model.base import Base
from app.schemas import Prompt

WORDS = [
            "apple", "bridge", "cloud", "dolphin", "engine", 
            "forest", "galaxy", "harbor", "igloo", "jungle", 
            "kite", "lantern", "mountain", "nebula", "ocean", 
            "pebble", "quartz", "river", "summit", "telescope", 
            "umbrella", "volcano", "whisper", "xylophone", "yacht", 
            "zenith", "anchor", "beacon", "crystal", "ember", 
            "feather", "glacier", "horizon", "illusion", "jewel", 
            "kinetic", "labyrinth", "mosaic", "nomad", "oasis", 
            "prism", "quantum", "radiate", "sapphire", "twilight", 
            "utopia", "velvet", "wander", "xenon", "yield"
        ]

class FakeModel(Base):
    async def generate(self, prompt: Prompt) -> AsyncIterable[str]:
        yield prompt.prompt + "\n"
        for _ in range(prompt.max_tokens):
            yield random.choice(WORDS) + " "