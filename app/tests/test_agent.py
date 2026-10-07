import pytest
from app.services.agent import ResearchAgent


@pytest.mark.asyncio
async def test_agent_research(mocker):
    mock_search = mocker.patch(
        "app.services.agent.web_search"
    )
    mock_document = mocker.patch(
        "app.services.agent.document_search"
    )

    mock_search.return_value = [
        {
            "title": "FastAPI",
            "url": "https://fastapi.tiangolo.com"
        }
    ]

    mock_document.return_value = []

    agent = ResearchAgent()

    result = await agent.run("What is FastAPI?")

    assert result is not None
    assert result["question"] == "What is FastAPI?"
    assert result["status"] == "completed"

    mock_search.assert_called_once_with("What is FastAPI?")
    mock_document.assert_called_once_with("What is FastAPI?")