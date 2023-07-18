from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    title: str
    description: Optional[str]


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    title: str
    description: Optional[str]
    category_id: int
    type: Optional[str]
    origin: Optional[str]
    certification: Optional[str]
    color: Optional[str]
    price: Optional[float]


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CategoryWithProducts(Category):
    products: List[Product] = []

    class Config:
        from_attributes = True
