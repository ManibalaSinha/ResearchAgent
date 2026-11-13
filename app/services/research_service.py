
from app.repositories.research_repository import ResearchRepository
from app.services.agent import ResearchAgent
from app.services.openai_service import generate_research_plan
class ResearchService:
   def __init__(self, agent: ResearchAgent,repository: ResearchRepository):
      self.agent = agent
      self.repository=repository
   async def research(self, question:str):
      #generate research plan using OpenAI
      result = await generate_research_plan(question)
      saved_result = await self.repository.create(question=result["question"], answer=result["answer"], status=result["status"])
      return saved_result
   async def get_by_id(self, research_id: int):
      return await self.repository.get_by_id(research_id)
