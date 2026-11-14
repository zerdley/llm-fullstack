import pytest

from app.dependencies import get_model
from app.main import app
from app.model.fake import FakeModel
from app.schemas import Prompt
from tests.fakes import get_no_yield_model


@pytest.mark.anyio
async def test_fake():
    prompt = Prompt(prompt="Hello", max_tokens=10)
    model = FakeModel()
    response = []
    async for token in model.generate(prompt):
        response.append(token)
    assert 1 <= len(response) <= 10


def test_generate(client):
    response = client.post("/generate", json={"prompt": "prompt", "max_tokens": 5})
    assert response.status_code == 200
    assert response.text == ("test" * 5)


def test_generate_log(client, generate_request_spy):
    response = client.post("/generate", json={"prompt": "prompt", "max_tokens": 5})
    assert response.status_code == 200
    assert len(generate_request_spy.calls) == 1
    prompt, ttft, total_gen_time, token_count = generate_request_spy.calls[0]
    assert prompt == Prompt(prompt="prompt", max_tokens=5)
    assert ttft >= 0
    assert total_gen_time >= 0
    assert total_gen_time >= ttft
    assert token_count == 5


def test_generate_no_max_tokens(client, generate_request_spy):
    response = client.post("/generate", json={"prompt": "prompt", "max_tokens": 0})
    assert response.status_code == 422
    assert len(generate_request_spy.calls) == 0


def test_generate_no_tokens(client, generate_request_spy):
    app.dependency_overrides[get_model] = get_no_yield_model
    response = client.post("/generate", json={"prompt": "prompt", "max_tokens": 10})
    assert response.status_code == 200
    assert len(generate_request_spy.calls) == 1
    _, ttft, _, token_count = generate_request_spy.calls[0]
    assert ttft is None
    assert token_count == 0
