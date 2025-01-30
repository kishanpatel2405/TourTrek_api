from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/api/v1/users/create", json={"name": "John", "email": "john@example.com", "password": "testpass"})
    assert response.status_code == 200
    assert response.json() == {"msg": "User created", "user": {"name": "John", "email": "john@example.com"}}
