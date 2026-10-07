import requests

class WebSearchError(Exception):
    pass
def web_search(question):
    return [
        {"title": "Result 1"},
        {"title": "Result 2"}
    ]

async def web_search(query: str):
    try:
        response = requests.get(
            "https://example.com/search",
            params={"q": query},
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("results", [])

    except Exception:
        return []