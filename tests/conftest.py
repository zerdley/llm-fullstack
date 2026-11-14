import pytest
from fastapi.testclient import TestClient

from app.dependencies import get_generate_request_logger, get_model
from app.main import app
from tests.fakes import GenerateRequestSpy, get_test_model


@pytest.fixture
def generate_request_spy() -> GenerateRequestSpy:
    return GenerateRequestSpy()


@pytest.fixture
def client(generate_request_spy):
    client = TestClient(app)
    app.dependency_overrides[get_model] = get_test_model
    app.dependency_overrides[get_generate_request_logger] = lambda: generate_request_spy
    yield client
    app.dependency_overrides.clear()
