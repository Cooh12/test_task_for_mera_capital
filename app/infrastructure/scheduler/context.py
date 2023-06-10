from dataclasses import dataclass

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.infrastructure.client.api import DeribitClient
from app.infrastructure.db.dao.holder import HolderDao


@dataclass
class ScheduledContextHolder:
    pool: async_sessionmaker[AsyncSession]
    client: DeribitClient


@dataclass
class ScheduledContext:
    dao: HolderDao
    client: DeribitClient
