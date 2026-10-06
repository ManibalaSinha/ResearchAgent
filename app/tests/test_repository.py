import pytest

from app.repositories.research_repository import ResearchRepository
@pytest.mark.asyncio
async def test_create_research(db_session):#passed
   repository = ResearchRepository(db_session)
   research = await repository.create(question="How to test FastAPI?", answer="install pytest", status="completed")
   assert research.id is not None
   assert research.answer == "install pytest"
   assert research.question == "How to test FastAPI?"
   assert research.status == "completed"
@pytest.mark.asyncio
async def test_get_research(db_session):#passed
   repository = ResearchRepository(db_session)
   created = await repository.create(question="How to test FastAPI?", answer="install pytest", status="completed")
   result= await repository.get_by_id(created.id)
   assert result is not None
   assert result.id == created.id

@pytest.mark.asyncio
async def test_get_research_not_found(db_session):#passed
   repository= ResearchRepository(db_session)
   result = await repository.get_by_id(0)
   assert result is None
