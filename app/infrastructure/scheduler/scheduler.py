from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.infrastructure.client.api import DeribitClient
from app.infrastructure.scheduler.context import ScheduledContextHolder
from app.infrastructure.scheduler.wrappers import add_new_values


class ApScheduler:
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        ScheduledContextHolder.pool = pool
        ScheduledContextHolder.client = DeribitClient()
        self.scheduler = AsyncIOScheduler()

    async def start(self):
        self.scheduler.start()
        await self.job()

    async def close(self):
        self.scheduler.shutdown()

    async def job(self):
        self.scheduler.add_job(add_new_values, 'interval', seconds=10)

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
