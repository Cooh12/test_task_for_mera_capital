import logging

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.infrastructure.scheduler import ApScheduler

logger = logging.getLogger(__name__)


def create_scheduler(pool: async_sessionmaker[AsyncSession]):
    return ApScheduler(pool=pool)
