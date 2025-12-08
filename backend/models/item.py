
# 1️⃣ Importamos los componentes necesarios de **SQLModel**.
#    - `SQLModel` es la clase base que combina las funcionalidades de
#      Pydantic (validación y serialización) y SQLAlchemy (ORM).
#    - `Field` permite definir metadatos de cada columna, como clave primaria,
#      valores por defecto, etc.
from sqlmodel import SQLModel, Field
# 2️⃣ Importamos `Optional` del módulo `typing`.
#    - Se usa para indicar que el atributo puede ser `None` (opcional) en
#      tiempo de creación del objeto. En la base de datos, esto permite que el
#      campo sea autogenerado (por ejemplo, un autoincremento).
from typing import Optional

# Modelo base (puede ser usado como DTO)
class ItemBase(SQLModel):
    name: str
    price: float = 0.0  # Por defecto es 0.0 si no se especifica

# Modelo para crear (sin ID)
class ItemCreate(ItemBase):
    pass

# Modelo de base datos
class ItemUpdate(SQLModel):
    name: Optional[str] = None
    price: Optional[float] = None

# 3️⃣ Definimos la clase [Item], que representa una tabla de la base de datos.
#    - Heredamos de `SQLModel` para que la clase sea tanto un modelo Pydantic
#      (para validación de entrada/salida) como un modelo SQLAlchemy (para
#      persistencia).
#    - El argumento `table=True` le indica a SQLModel que debe crear una tabla
#      llamada [item] (el nombre se genera automáticamente a partir del nombre
#      de la clase, en minúsculas) cuando ejecutemos `SQLModel.metadata.create_all`.
class Item(ItemBase, table=True):
        # 4️⃣ Campo `id`:
    #    - Tipo `Optional[int]`: puede ser `int` o `None`. Cuando se crea un
    #      objeto sin especificar `id`, se le asigna `None` y la base de datos
    #      lo reemplaza por un valor autoincremental.
    #    - `Field(default=None, primary_key=True)`: indica que este campo es la
    #      **clave primaria** de la tabla y que su valor por defecto es `None`
    #      (para que la base de datos lo genere)
    id: Optional[int] = Field(default=None, primary_key=True)