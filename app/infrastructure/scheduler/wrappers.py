import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator

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
    async with prepare_context() as context:  # type: ScheduledContext
        tasks = [add_new_value_btc(context), add_new_value_eth(context)]
        await asyncio.gather(*tasks)
        await context.dao.session.commit()


async def add_new_value_btc(context: ScheduledContext) -> None:
    value = await context.client.get_index_price_for_btc()
    context.dao.btc._save(value.to_db)


async def add_new_value_eth(context: ScheduledContext) -> None:
    value = await context.client.get_index_price_for_eth()
    context.dao.eth._save(value.to_db)
