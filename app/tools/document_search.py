import asyncio

class DocumentSearchError(Exception):pass
async def document_search(query:str):
   try:
      await asyncio.sleep(.05)
      if "failure" in query.lower():
         raise DocumentSearchError("Document Search Timed out")
      return f"Document Search :{query}"
   except TimeoutError as exc:
      raise DocumentSearchError(str(exc)) from exc 