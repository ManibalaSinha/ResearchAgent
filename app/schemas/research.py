from pydantic import BaseModel, Field
class ResearchRequest(BaseModel):
   question: str = Field(min_length=3, max_length=200)
class ResearchResponse(BaseModel):
   id: int
   question: str
   answer: str
   status: str

