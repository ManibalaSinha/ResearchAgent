from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from app.main import app
from app.tools.web_search import WebSearchError
from app.tools.document_search import DocumentSearchError
client = TestClient(app)
def test_research_health():
   response=client.get("/research/health")
   assert response.status_code==200
   assert response.json()=={"status":"ok"}
@patch("app.routes.research.ResearchRepository")
@patch("app.routes.research.ResearchAgent")
def test_create_research_success(mock_agent_class, mock_repository_class,):
   mock_agent = mock_agent_class.return_value
   mock_agent.run= AsyncMock(return_value="Web research:AI\nDocument research:AI")
   mock_result= type("ReserchResult",(),{"id":1,"question":"What is AI?","answer":"Web research:AI\nDocument research:AI","status":"completed",},)()
   mock_repository = mock_repository_class.return_value
   mock_repository.create= AsyncMock(return_value= mock_result)
   response = client.post("/research", json={"question":"What is AI?"},)
   assert response.status_code == 200
   assert response.json()=={"id":1,"question":"What is AI?","answer":"Web research:AI\nDocument research:AI", "status":"completed",}
   mock_agent.run.assert_awaited_once_with("What is AI?")
   mock_repository.create.assert_awaited_once_with(question="What is AI?", answer="Web research:AI\nDocument research:AI", status="completed",)
   def test_create_research_invalid_question():
      response = client.post("/research",json={"question":"AI"},)
      assert response.status_code==422
   @patch("app.routes.reserch.ResearchAgent")
   def test_web_search_failure(mock_agent_class):
      mock_agent=mock_agent_class.return_value
      mock_agent.run=AsyncMock(side_effect=WebSearchError("Web search timed out"))
      response = client.post("/research", json={"question":"What is AI?"},)
      assert response.status_code==503
      assert response.json()=={"detail":"Research serice temporarily unavailable"}
   @patch("app.routes.research.ResearchAgent")
   def test_document_search_failure(mock_agent_class):
      mock_agent= mock_agent_class.return_value
      mock_agent.run=AsyncMock(side_effect=DocumentSearchError("Document search service failed"))
      response=client.post("/research", json={"question":"What is AI?"},)
      assert response.status_code==503
      assert response.json()=={"detail":"Research service temporarilly unavailable"}