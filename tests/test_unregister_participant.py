# tests/test_unregister_participant.py
import pytest

def test_unregister_success(client):
    # Arrange
    activity = "Chess Club"
    email = "daniel@mergington.edu"
    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 200
    assert f"Removed {email}" in response.json()["message"]
    # Confirm participant removed
    get_resp = client.get("/activities")
    assert email not in get_resp.json()[activity]["participants"]


def test_unregister_nonexistent_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "notfound@mergington.edu"
    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_unregister_nonexistent_activity(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "someone@mergington.edu"
    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
