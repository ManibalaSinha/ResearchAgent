from app.tools.web_search import web_search
import pytest
@pytest.mark.asyncio
async def test_web_search_success(mocker):
   mock_response = mocker.Mock()
   mock_response.json.return_value ={"results":[{"title":"What is FastAPI?", "url":"https://fastapi.tiangolo.com"}]}
   mock_response.raise_for_status.return_value=None
   mocker.patch("requests.get", return_value=mock_response)
   result = await web_search("What is FastAPI?")
   assert len(result) ==1
   assert result[0]["title"]=="What is FastAPI?"

@pytest.mark.asyncio
async def test_web_search_failure(mocker):
   mocker.patch("requests.get", side_effect=Exception("Search API failed"))
   result = await web_search("What is FastAPI?")
   assert result == []

@pytest.mark.asyncio
async def test_web_search_empty(mocker):
   mock_response = mocker.Mock()
   mock_response.json.return_value = {"results": []}
   mock_response.raise_for_status.return_value = None
   mocker.patch("requests.get", return_value=mock_response)
   result =await web_search("What is FastAPI?")
   assert result == []

