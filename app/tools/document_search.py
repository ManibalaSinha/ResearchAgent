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


