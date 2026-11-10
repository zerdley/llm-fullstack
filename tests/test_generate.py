from app.model.fake import FakeModel
from app.models import Prompt
import pytest

@pytest.mark.anyio
async def test_generate():
    prompt = Prompt(prompt="Hello", max_tokens=10)
    model = FakeModel()
    response = []
    async for token in model.generate(prompt):
        response.append(token)
    assert(len(response)==11)
    assert(response[0]=="Hello\n")