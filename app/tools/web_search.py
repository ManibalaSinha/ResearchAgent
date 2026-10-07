import requests

class WebSearchError(Exception):
    pass


async def web_search(query: str):
    return [
        {
            "title": f"FastAPI information for: {query}",
            "url": "https://fastapi.tiangolo.com/",
            "snippet": "FastAPI is a modern Python web framework for building APIs."
        },
        {
            "title": "FastAPI Documentation",
            "url": "https://fastapi.tiangolo.com/",
            "snippet": "FastAPI is based on Python type hints and provides automatic API documentation."
        }
    ]