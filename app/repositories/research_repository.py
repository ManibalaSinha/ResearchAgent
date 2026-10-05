from app.models.research import ResearchResult
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
class ResearchRepository:
   def __init__(self, db: AsyncSession):
      self.db=db
   async def create(self, question:str, answer:str, status:str):
      result = ResearchResult(question=question, answer=answer, status=status,)
      self.db.add(result)
      await self.db.commit()
      await self.db.refresh(result)
      return result
   async def get_by_id(self, research_id:int):
      result=await self.db.execute(select(ResearchResult).where(ResearchResult.id == research_id))
      return result.scalar_one_or_none()