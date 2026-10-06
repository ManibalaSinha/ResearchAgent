from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)
def test_health():#passed
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_research_success(mocker):#fail
    response = client.post( "/research",        json={"question": "What is FastAPI?"}    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "answer" in data
