from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from src.settings.database import get_async_session
from src.product import models, schemas


router = APIRouter(prefix="/product", tags=["product"])


@router.get("/", response_model=schemas.ProductBase)
async def get_products(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    session: AsyncSession = Depends(get_async_session),
) -> list[schemas.ProductBase]:
    sql = select(models.Product).order_by(models.Product.id).limit(limit).offset(offset)
    db_products = (await session.execute(sql)).scalars().unique().all()
    return db_products


@router.post("/")
async def add_specific_product(
    schema: schemas.ProductCreate, session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(models.Product).values(**schema.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/{product_id}", response_model=schemas.ProductBase)
async def get_product(
    product_id: int, session: AsyncSession = Depends(get_async_session)
) -> list[schemas.ProductBase]:
    sql = select(models.Product).where(models.Product.id == product_id)
    db_product = (await session.execute(sql)).scalars().all()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
