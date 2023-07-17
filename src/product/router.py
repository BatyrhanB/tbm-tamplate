from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.settings.database import get_async_session
from src.product import models


router = APIRouter(prefix="/product", tags=["product"])


@router.get("/")
async def get_specific_operations(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    session: AsyncSession = Depends(get_async_session),
):
    sql = select(models.Product).order_by(models.Product.id).limit(limit).offset(offset)
    db_products = (await session.execute(sql)).scalars().unique().all()
    return db_products
