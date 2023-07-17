from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from src.settings.base_model import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="products")
    type = Column(String, index=True, nullable=True)
    origin = Column(String, index=True, nullable=True)
    certification = Column(String, index=True, nullable=True)
    color = Column(String, index=True, nullable=True)
    price = Column(Float, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
