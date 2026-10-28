from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_hello_world():
    """Корневой эндпоинт возвращает приветствие."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World from Backend!"}


def test_health_check():
    """Health-check возвращает статус ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_swagger_docs_available():
    """Swagger UI доступен на /docs (OpenAPI генерируется автоматически)."""
    response = client.get("/docs")
    assert response.status_code == 200

    openapi = client.get("/openapi.json")
    assert openapi.status_code == 200
    assert openapi.json()["info"]["title"] == "Hello World API"