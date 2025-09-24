from pydantic import BaseModel, HttpUrl
from typing import Optional
from models import CategoryType, UOMType
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    category: CategoryType
    description: Optional[str] = None
    product_image: Optional[HttpUrl] = None
    sku: str
    unit_of_measure: UOMType
    lead_time: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True  # for Pydantic V2
