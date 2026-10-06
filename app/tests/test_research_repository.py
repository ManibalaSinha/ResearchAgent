from unittest.mock import AsyncMock
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)
def test_research_repository(mock_repository_class,):
   mock_repository.get_by_id=AsyncMock(return_value=None)
   response=client.get("/research/999")
   assert response.status_code == 404
   assert response.json()=={"detail":"Research result not found"}