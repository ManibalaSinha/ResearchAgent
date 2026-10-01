from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database.connection.base import Base

class ResearchResult(Base):
   __tablename__="research_results"
   id:Mapped[int]= mapped_column(Integer,primary_key = True,)
   question:Mapped[str]= mapped_column(String(2000), nullable=False,)
   answer:Mapped[str]= mapped_column(Text, nullable=False,)
   status:Mapped[datetime]= mapped_column(DateTime, default=datetime.utcnow, nullable=False,)

