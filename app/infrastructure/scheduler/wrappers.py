import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator

from app.core.models.enums.tickers import Ticker
from app.infrastructure.db.dao.holder import HolderDao
from app.infrastructure.scheduler.context import ScheduledContext, ScheduledContextHolder


@asynccontextmanager
async def prepare_context() -> AsyncIterator[ScheduledContext]:
    async with ScheduledContextHolder.pool() as session:
        dao = HolderDao(
            session=session
        )
        yield ScheduledContext(
            dao=dao,
            client=ScheduledContextHolder.client
        )


async def add_new_values() -> None:
    tasks = (add_new_value(ticker.value) for ticker in Ticker)
    await asyncio.gather(*tasks)


async def add_new_value(ticker: str) -> None:
    async with prepare_context() as context:  # type: ScheduledContext
        result = await context.client.get_index_price(ticker)
        context.dao.coin._save(result.to_db)
        await context.dao.coin.commit()
