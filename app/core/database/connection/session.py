from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker,create_async_engine
from app.core.config.settings import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    class_= AsyncSession,
    expire_on_commit=False,
    bind=engine,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session