
from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from src.settings.base_model import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")
    type = Column(String, index=True)
    origin = Column(String, index=True)
    certification = Column(String, index=True)
    color = Column(String, index=True)
    price = Column(Float)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
