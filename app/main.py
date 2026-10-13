from fastapi import FastAPI
from app.routes import research
import logging
from fastapi import Request
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app= FastAPI()
@app.exception_handler(Exception)
async def log_unhandled_exception(request: Request, exc: Exception):
    logger.exception(
        "Unhandled error on %s %s",
        request.method,
        request.url.path,
        exc_info=exc,
    )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error. Check the terminal."},
    )
@app.get("/health")
def health():
   return {"status": "ok"}
app.include_router(research.router,prefix="/research", tags=["Research"])