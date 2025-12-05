from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers.item import router as item_router
from app.db import init_db

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
app.include_router(item_router)

