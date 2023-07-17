from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.settings.config import settings
from src.auth import User


engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, future=True, echo=True,
                             execution_options={"isolation_level": "AUTOCOMMIT"})

async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    print("HEREEEE", settings.SQLALCHEMY_DATABASE_URI)
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)