from fastapi import APIRouter,Depends, HTTPException
router = APIRouter()
@router.get("/health")
async def reserch_health():
   return {"status": "research service available"}
