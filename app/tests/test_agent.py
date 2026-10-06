from unittest.mock import AsyncMock
import pytest
from app.services.agent import ResearchAgent
from app.tools import web_search

@pytest.mark.asyncio
async def test_agent_research(mocker):
   mock_search = mocker.patch("app.agents.research_agent.web_search")
   mock_search.return_value= [{"title": "FastAPI", "url": "https://fastapi.tiangolo.com"}]
   agent= ResearchAgent()
   result=await agent.research("What is FastAPI?")
   assert result is not None
   mock_search.assert_called_once()



   