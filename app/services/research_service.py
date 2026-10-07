from app.services.agent import ResearchAgent
class ResearchService:
   def __init__(self, agent, repository):
      self.agent = agent
      self.repository=repository
   async def research(self, question):
      result = await self.agent.run(question)
      saved_result = await self.repository.create(question=result["question"], answer=result["answer"], status=result["status"])
      return saved_result
   async def get_by_id(self, research_id: int):
      return await self.repository.get_by_id(research_id)
