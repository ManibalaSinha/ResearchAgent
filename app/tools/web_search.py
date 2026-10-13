import requests, os
from tavily import TavilyClient
class WebSearchError(Exception):
    pass
async def web_search(query: str):
    try:
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            raise WebSearchError("TAVILY_API_KEY is not set")
        client = TavilyClient(api_key=api_key)
        response = client.search(query=query, max_results=5)
        return response.get("results", [])
    except Exception as e:
        raise WebSearchError(f"Web search failed: {e}") from e
        