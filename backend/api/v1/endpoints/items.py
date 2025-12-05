# app/routers/item.py – Router para operaciones CRUD de Items

from fastapi import APIRouter, HTTPException
from typing import List
from models.item import Item, ItemCreate
# Importamos `select` para consultas SQLModel y nuestra fábrica de sesiones async
from sqlmodel import select
from core.db import async_session

# 1️⃣ Definimos el router
router = APIRouter(tags=["items"])


@router.get("/", response_model=List[Item])
async def list_items():
    async with async_session() as session:
        # Usamos .execute() (estándar SQLAlchemy) en lugar de .exec()
        result = await session.execute(select(Item))
        # .scalars() extrae los objetos del resultado
        items = result.scalars().all()
        return items

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):  # Aquí 'item' es el parámetro de la función, de tipo 'Item' (el modelo Pydantic/SQLModel)
    async with async_session() as session:  # Inicia una sesión asíncrona con la base de datos
        db_item = Item.model_validate(item)
        session.add(db_item)
        await session.commit()
        await session.refresh(db_item)
        return db_item

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    async with async_session() as session:
        result = await session.execute(select(Item).where(Item.id == item_id))
        db_item = result.scalars().first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, updated: Item):
    async with async_session() as session:
        result = await session.execute(select(Item).where(Item.id == item_id))
        db_item = result.scalars().first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        db_item.name = updated.name
        db_item.price = updated.price
        
        session.add(db_item)
        await session.commit()
        await session.refresh(db_item)
        return db_item


@router.delete("/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    async with async_session() as session:
        result = await session.execute(select(Item).where(Item.id == item_id))
        db_item = result.scalars().first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        await session.delete(db_item)
        await session.commit()
        return {"detail": "Item deleted"}

