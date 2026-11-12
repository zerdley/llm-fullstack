from app.model.fake import FakeModel
from app.schemas import Prompt
import pytest

@pytest.mark.anyio
async def test_fake():
    prompt = Prompt(prompt="Hello", max_tokens=10)
    model = FakeModel()
    response = []
    async for token in model.generate(prompt):
        response.append(token)
    assert len(response)==11 
    assert response[0]=="Hello\n" 


def test_generate(client):
    response = client.post(
        "/generate",
        json={"prompt": "prompt", "max_tokens": 5}
        )
    assert response.status_code == 200
    assert response.text == "prompt" + ("test" * 5)

def test_generate_log(client, generate_request_spy):
    response = client.post(
        "/generate",
        json={"prompt": "prompt", "max_tokens": 5}
        )
    assert response.status_code == 200
    assert generate_request_spy.calls == [Prompt(prompt='prompt', max_tokens=5)]