from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from src.settings.database import get_async_session
from src.product import models, schemas


router = APIRouter(prefix="/product", tags=["product"])
category_router = APIRouter(prefix="/category", tags=["category"])


@router.get("/")
async def get_products(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    session: AsyncSession = Depends(get_async_session),
) -> list[schemas.Product]:
    sql = select(models.Product).order_by(models.Product.id).limit(limit).offset(offset)
    db_products = (await session.execute(sql)).scalars().unique().all()
    return db_products


@router.post("/")
async def create_product(
    schema: schemas.ProductCreate, session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(models.Product).values(**schema.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/{product_id}")
async def get_product(
    product_id: int, session: AsyncSession = Depends(get_async_session)
) -> list[schemas.Product]:
    sql = select(models.Product).where(models.Product.id == product_id)
    db_product = (await session.execute(sql)).scalars().all()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@category_router.post("/")
async def create_category(
    schema: schemas.CategoryCreate, session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(models.Category).values(**schema.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@category_router.get("/")
async def get_categories(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    session: AsyncSession = Depends(get_async_session),
) -> list[schemas.Category]:
    sql = select(models.Category).order_by(models.Category.id).limit(limit).offset(offset)
    db_category= (await session.execute(sql)).scalars().unique().all()
    return db_category 


@category_router.get("/{category_id}")
async def get_category(
    category_id: int, session: AsyncSession = Depends(get_async_session)
) -> list[schemas.Category]:
    sql = select(models.Category).where(models.Category.id == category_id)
    db_category = (await session.execute(sql)).scalars().all()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category