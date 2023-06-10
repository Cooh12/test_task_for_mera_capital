import logging


from sqlalchemy import make_url
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from app.infrastructure.db import DBConfig

logger = logging.getLogger(__name__)


def create_session_maker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    pool: async_sessionmaker[AsyncSession] = async_sessionmaker(
        bind=engine, expire_on_commit=False, autoflush=False
    )
    return pool


def create_engine(config: DBConfig) -> AsyncEngine:
    return create_async_engine(url=make_url(config.uri), echo=config.echo)


