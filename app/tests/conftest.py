from decouple import config
import pytest
from fastapi.testclient import TestClient
from app.main import app

API_KEY = config("API_KEY")


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def auth_headers():
    return {
        "X-API-Key": API_KEY
    }
