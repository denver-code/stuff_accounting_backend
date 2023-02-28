from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from app.core.config import settings
from app.core.tools.jwt import FastJWT

from v1.api import v1_router


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()

@app.on_event("startup")
async def on_startup():
    FastJWT().set_secret_key(settings.JWT_SECRET_KEY)

@app.get("/")
async def showcase_event():
    return {
        "project_name": settings.PROJECT_NAME,
        "message": "Welcome on our server, stranger!",
        "docs": "/v1/etc/docs",
        "server_time": str(datetime.now())
        
    }

app.include_router(v1_router)