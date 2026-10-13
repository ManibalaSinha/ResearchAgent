import asyncio

class DocumentSearchError(Exception): pass
DOCUMENTS = [
    "FastAPI is a Python framework for building APIs.",
    "FastAPI supports asynchronous endpoints.",
    "PostgreSQL is a relational database."
]
async def document_search(query: str):
   words = set(query.lower().split())
   return [document for document in DOCUMENTS if words.intersection(document.lower().split())]
""" async def document_search(query: str):
   try:
      
      if not query.strip():
         raise DocumentSearchError("Query cannot be empty")
      words = set(query.lower().split())
      results = [
         document for document in DOCUMENTS
         if words.intersection(document.lower().split())
      ]
   except DocumentSearchError:
      raise
   except Exception as e:
      raise DocumentSearchError(f"Document search failed: {e}") from e """

