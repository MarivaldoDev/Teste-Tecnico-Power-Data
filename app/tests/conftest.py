import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

API_KEY = os.getenv("API_KEY", "powerofdata-key")


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def auth_headers():
    return {
        "API-Key": API_KEY
    }
