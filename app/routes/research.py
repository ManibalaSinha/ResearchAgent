from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.connection.session import get_db
from app.schemas.research import ResearchResponse, ResearchRequest
from app.services.research_service import ResearchService
from app.services.agent import ResearchAgent
from app.repositories.research_repository import ResearchRepository
from app.tools.document_search import DocumentSearchError
from app.tools.web_search import WebSearchError
from sqlalchemy import text

router = APIRouter()
@router.get("/health")
async def reserch_health():
   return {"status": "ok"}

@router.post("",response_model=ResearchResponse)
async def create_research(request:ResearchRequest, db:AsyncSession=Depends(get_db),):
   repository= ResearchRepository(db)
   agent = ResearchAgent()
   service=ResearchService(agent=agent,repository=repository,)
   try:
      result = await service.research(request.question)
   except(WebSearchError, DocumentSearchError):
      raise HTTPException(status_code=503,detail="Research service temporarily unavailable")
   return ResearchResponse(id=result.id, question=result.question, answer=result.answer, status=result.status)



""" @router.get("/test-db")
async def test_db(db:AsyncSession = Depends(get_db)):
   result = await db.execute(text("SELECT 1"))
   return {"database":"connected", "result": result.scalar(),} """
@router.get("/test-repository/{research_id}")
async def test_repository(research_id: int, db: AsyncSession = Depends(get_db),):
    repository = ResearchRepository(db)
    result = await repository.get_by_id(research_id)
    if result is None:
        return {            "found": False,
            "research_id": research_id,        }
    return {
        "found": True,
        "id": result.id,
        "question": result.question,
        "status": result.status,    }
@router.get("/{research_id}", response_model=ResearchResponse)
async def get_research(research_id:int, db:AsyncSession = Depends(get_db)):
   repository = ResearchRepository(db)
   agent= ResearchAgent()
   service= ResearchService(agent=agent,repository=repository,)
   result = await service.get_by_id(research_id)
   if result is None:
      raise HTTPException(status_code=404,detail="Research not found",)
   return ResearchResponse(id=result.id, question=result.question, answer=result.answer, status=result.status)
#@router.get()

