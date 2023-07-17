from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    title: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    title: str
    description: str
    category_id: int
    type: str
    origin: str
    certification: str
    color: str
    price: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: datetime
    category: Category

    class Config:
        orm_mode = True


class CategoryWithProducts(Category):
    products: List[Product] = []

    class Config:
        orm_mode = True