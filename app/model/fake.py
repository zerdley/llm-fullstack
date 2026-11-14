import asyncio
import random
from collections.abc import AsyncIterable

from app.config import settings
from app.model.base import Base
from app.schemas import Prompt

WORDS = [
    "apple",
    "bridge",
    "cloud",
    "dolphin",
    "engine",
    "forest",
    "galaxy",
    "harbor",
    "igloo",
    "jungle",
    "kite",
    "lantern",
    "mountain",
    "nebula",
    "ocean",
    "pebble",
    "quartz",
    "river",
    "summit",
    "telescope",
    "umbrella",
    "volcano",
    "whisper",
    "xylophone",
    "yacht",
    "zenith",
    "anchor",
    "beacon",
    "crystal",
    "ember",
    "feather",
    "glacier",
    "horizon",
    "illusion",
    "jewel",
    "kinetic",
    "labyrinth",
    "mosaic",
    "nomad",
    "oasis",
    "prism",
    "quantum",
    "radiate",
    "sapphire",
    "twilight",
    "utopia",
    "velvet",
    "wander",
    "xenon",
    "yield",
]


class FakeModel(Base):
    async def generate(self, prompt: Prompt) -> AsyncIterable[str]:
        for _ in range(random.randrange(1, prompt.max_tokens + 1)):
            yield random.choice(WORDS) + " "
            await asyncio.sleep(settings().fake_sleep_time)
