import pytest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.config.settings import settings


@pytest.fixture
async def db_session():
    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=False
    )

    SessionLocal = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with SessionLocal() as session:
        yield session

    await engine.dispose()