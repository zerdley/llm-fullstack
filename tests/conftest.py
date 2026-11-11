from typing import AsyncIterable

import pytest
from app.dependencies import get_model
from app.model.base import Base
from app.schemas import Prompt
from fastapi.testclient import TestClient
from app.main import app

def get_test_model():
    return StubModel()

class StubModel(Base):
    async def generate(self, prompt: Prompt) -> AsyncIterable[str]:
        yield prompt.prompt
        for _ in range(prompt.max_tokens):
            yield "test"

@pytest.fixture
def client():
    client = TestClient(app)
    app.dependency_overrides[get_model] = get_test_model
    yield client
    app.dependency_overrides.clear()