from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "total": 0,
        "skip": 0,
        "limit": 10,
        "items": []
    }


def test_delete_nonexistent_item():
    response = client.delete("/tasks/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Tarefa com ID 1 não encontrada"}


def test_post_item():
    response = client.post("/tasks", json={
        "title": "Minha primeira tarefa",
        "description": "Testar a API",
        "completed": False
    })
    assert response.status_code == 201

    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Minha primeira tarefa"
    assert data["description"] == "Testar a API"
    assert data["completed"] is False
    assert "created_at" in data


def test_get_item():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Minha primeira tarefa"
    assert "created_at" in data


def test_delete_existent_item():
    response = client.delete("/tasks/1")
    assert response.status_code 