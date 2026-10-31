from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "My First App" in response.text


def test_hello():
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "<h1>Hello</h1>" in response.text


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_pod(monkeypatch):
    monkeypatch.setattr(main.socket, "gethostname", lambda: "test-pod")

    response = client.get("/pod")

    assert response.status_code == 200
    assert response.json() == {"pod": "test-pod"}

