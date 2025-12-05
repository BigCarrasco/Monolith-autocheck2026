from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.v1.endpoints.items import router as item_router
from core.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield #hold on and cleaning up

app = FastAPI(
    title="AutoCheck", 
    description="API para gestionar vehículos", 
    version="1.0.0", 
    lifespan=lifespan)


# Include the item CRUD router
app.include_router(item_router, prefix="/api/v1", tags=["items"])

