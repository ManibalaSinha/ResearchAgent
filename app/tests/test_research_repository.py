
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@patch("app.routes.research.ResearchRepository")
def test_research_repository(mock_repository_class):
    mock_repository = mock_repository_class.return_value
    mock_repository.get_by_id = AsyncMock(return_value=None)

    response = client.get("/research/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Research not found"
    }

    mock_repository.get_by_id.assert_awaited_once_with(999)

