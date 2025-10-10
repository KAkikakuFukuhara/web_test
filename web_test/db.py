from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine

SQLITE_SYNC_URL_PREFIX = "sqlite:///"
SQLITE_ASYNC_URL_PREFIX = "sqlite+aiosqlite:///"
FILE_PATH = "fastapi_app.db"

engine: AsyncEngine = create_async_engine(SQLITE_ASYNC_URL_PREFIX+FILE_PATH)
SessionLocal= sessionmaker(bind=engine, class_=AsyncSession)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session
