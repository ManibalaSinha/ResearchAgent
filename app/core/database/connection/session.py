from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database.connection.session import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

