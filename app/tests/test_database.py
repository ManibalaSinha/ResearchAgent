import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database.connection.session import AsyncSessionLocal
@pytest.mark.asyncio
async def test_database_session():
   async with AsyncSessionLocal() as session:
      assert isinstance(session, AsyncSession)