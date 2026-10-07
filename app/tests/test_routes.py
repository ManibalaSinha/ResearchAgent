from fastapi.testclient import TestClient
from app.main import app
from app.tools.web_search import web_search
from types import SimpleNamespace
from unittest.mock import AsyncMock

client = TestClient(app)
def test_health():#passed
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_research_success(mocker):#fail
    mock_service = mocker.patch("app.routes.research.ResearchService")
    mock_service.return_value.research = AsyncMock(
        return_value=SimpleNamespace(
        id=1,
        question= "What is FastAPI?",
        answer= "FastAPI is a Python web framework.",
        status= "completed",)
    )
    response = client.post("/research", json={"question":"What is FastAPI?"})
    assert response.status_code == 200
def test_create_research_invalid_request():
    response = client.post("/research", json={})
    assert response.status_code == 422

   
