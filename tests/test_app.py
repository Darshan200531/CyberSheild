import pytest
from app import create_app

@pytest.fixture()
def client(tmp_path):
    db_path = tmp_path / "test.db"
    app = create_app({
        "TESTING": True,
        "DATABASE_PATH": str(db_path),
        "SECRET_KEY": "test-secret"
    })
    return app.test_client()

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"CyberShield Mini SIEM" in response.data

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

def test_unknown_route(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404
