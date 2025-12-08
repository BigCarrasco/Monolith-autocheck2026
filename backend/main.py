from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the item CRUD router
app.include_router(item_router, prefix="/api/v1/items", tags=["items"])

