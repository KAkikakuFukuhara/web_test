import asyncio

from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import AsyncEngine

from web_test.db import engine, Base


def reset_database():
    if isinstance(Base, DeclarativeMeta):
        if isinstance(engine, Engine):
            Base.metadata.drop_all(bind=engine)
            Base.metadata.create_all(bind=engine)
        else:
            raise Exception
    else:
        raise Exception


async def reset_async_database():
    if isinstance(Base, DeclarativeMeta):
        if isinstance(engine, AsyncEngine):
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.drop_all)
                await conn.run_sync(Base.metadata.create_all)
        else:
            raise Exception
    else:
        raise Exception


if __name__ == "__main__":
    asyncio.run(reset_async_database())
