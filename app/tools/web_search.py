import asyncio


class WebSearchError(Exception):pass
async def search(query:str):
   try:
      await asyncio.sleep(.05)
      if "failure" in query.lower():
         raise WebSearchError("web search timed out")
      return f"Web results for:{query}"
   except TimeoutError as exc:
      raise WebSearchError(str(exc)) from exc