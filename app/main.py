from fastapi import FastAPI
from app.routes import research
app= FastAPI()
@app.get("/health")
def health():
   return {"status": "ok"}
app.include_router(research.router,prefix="/research", tags=["Research"])