from app.tools.web_search import web_search 
from app.tools.document_search import document_search
class ResearchAgent:
   def __init__(self):
      self.tools={"web_search": web_search, "document_search":document_search}
   async def run(self, question):
      web_result = await self.tools["web_search"](question)
      document_result= await self.tools["document_search"](question)
    
      return { "question" : question, "answer" : (f"Web research:{web_result}\n" f"Document search:{document_result}"), "status" : "completed"}
   
