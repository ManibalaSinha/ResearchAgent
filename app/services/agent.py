from app.tools import document_search, web_search 
class ResearchAgent:
   def __init__(self):
      self.tools={"web_search": web_search, "document_search":document_search}
   async def run(self, question:str):
      web_result = await self.tools["web_search"](question)
      document_result= await self.tools["document_search"](question)
      answer = (f"Web research:{web_result}\n" f"Document search:{document_result}")
      return { "question" : question, "answer" : answer, "status" : "completed"}
   
