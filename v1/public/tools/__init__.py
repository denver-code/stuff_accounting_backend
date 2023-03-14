from fastapi import APIRouter, Depends, HTTPException
from app.core.tools.jwt import FastJWT

tools_router = APIRouter(prefix="/tools")

@tools_router.get("/verify/", dependencies=[Depends(
        FastJWT().login_required
        )])
async def verify_token_event():
    return {"message": "Token are valid!"}