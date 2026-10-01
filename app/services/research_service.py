from app.services.agent import ResearchAgent
class ReserchService:
   def __init__(self, agent:ResearchAgent):
      self.agent = agent
   async def research(self, question:str):
      result =  await self.agent.run(question)
      return result
