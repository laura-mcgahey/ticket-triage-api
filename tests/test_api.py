from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ticket_with_empty_subject_is_rejected():
    response = client.post("/tickets", json={"subject": "", "body": "Something"})
    assert response.status_code == 422