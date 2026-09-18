from fastapi.testclient import TestClient

from main import app


def test_health_endpoint_reports_process_status() -> None:
    """The basic service is observable before external dependencies exist."""

    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "VeriRAG",
        "environment": "development",
    }