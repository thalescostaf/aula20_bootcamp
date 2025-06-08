from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

    @validator("categoria")
    def check_categoria(cls, v):
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")

class ProductCreate(ProductBase):
    pass
