from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_known_flight():
    assert client.get("/flights/ai101").json()["status"] == "On time"
