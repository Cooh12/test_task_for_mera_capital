from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.core.interfaces.db_provaider_protocol import dao
from .db import DbProvider


def setup_providers(app: FastAPI, pool: async_sessionmaker[AsyncSession]):
    db_provider = DbProvider(pool=pool)

    app.dependency_overrides[dao] = db_provider.dao
