# tests/test_get_activities.py
from fastapi.testclient import TestClient
from src.app import app

def test_get_activities_returns_all(client):
    # Arrange
    # (client fixture provided by conftest.py)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert all("participants" in v for v in data.values())
