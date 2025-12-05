# app/db.py – Configuración y utilidades de base de datos async

# 1️⃣ Importamos los componentes necesarios de SQLModel y SQLAlchemy
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# 2️⃣ URL de conexión a la base de datos SQLite usando el driver async `aiosqlite`
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# 3️⃣ Motor async
#    - Usamos `create_async_engine` para garantizar compatibilidad con `async with`
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# 4️⃣ Fábrica de sesiones async
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# 5️⃣ Función de inicialización de la base de datos
async def init_db() -> None:
    """Create database tables on startup if they don't exist."""
    async with engine.begin() as conn:
        # run_sync permite ejecutar métodos síncronos (como create_all) en el contexto async
        await conn.run_sync(SQLModel.metadata.create_all)
