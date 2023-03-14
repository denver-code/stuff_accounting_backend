from fastapi import APIRouter
from v1.public.authorisation import authorisation_router
from v1.public.tools import tools_router

public_router = APIRouter(prefix="/public")

public_router.include_router(authorisation_router)
public_router.include_router(tools_router)