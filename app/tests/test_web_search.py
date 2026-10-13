from app.tools.web_search import WebSearchError, web_search
import pytest

@pytest.mark.asyncio
async def test_web_search_success(mocker):
   mock_client = mocker.Mock()
   mock_client.search.return_value ={"results":[{"title":"What is FastAPI?", "url":"https://fastapi.tiangolo.com"}]}
  
   mocker.patch("app.tools.web_search.TavilyClient", return_value=mock_client)
   result = await web_search("What is FastAPI?")
   assert len(result) == 1
   assert result[0]["title"]=="What is FastAPI?"
   assert result[0]["url"] == "https://fastapi.tiangolo.com"

@pytest.mark.asyncio
async def test_web_search_empty(mocker):
   mock_client = mocker.Mock()
   mock_client.search.return_value = {"results": []}
   mock_client.raise_for_status.return_value = None
   mocker.patch("app.tools.web_search.TavilyClient", return_value=mock_client)
   result =await web_search("What is FastAPI?")
   assert result == []

@pytest.mark.asyncio
async def test_web_search_failure(mocker):
   mock_client = mocker.Mock()
   mock_client.search.side_effect = Exception("Search API failed")
   mocker.patch("app.tools.web_search.TavilyClient", return_value=mock_client)
   with pytest.raises(WebSearchError, match="Web search failed"):
      await web_search("What is FastAPI?")

@pytest.mark.asyncio
async def test_web_search_missing_api_key(mocker):
   mocker.patch.dict("os.environ", {}, clear = True)
   with pytest.raises(WebSearchError, match="TAVILY_API_KEY is not set"):
      await web_search("What is FastaPI")

