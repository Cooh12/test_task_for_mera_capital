from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from ...models import Ticker


class TickerDAO(BaseDAO[Ticker]):
    def __init__(self, session: AsyncSession):
        super().__init__(Ticker, session)

    async def get_curent_price(self, coin_name: str) -> Ticker:
        result = await self.session.execute(
            select(Ticker).where(Ticker.coin_name == coin_name).order_by(Ticker.id.desc()).limit(1))
        return result.scalar_one()

    async def get_all_values(self, coin_name: str, date_from: float | None, date_to: float | None) -> list[Ticker]:
        query = select(Ticker).where(Ticker.coin_name == coin_name)
        print(date_from, date_to)
        if date_from and date_to:
            query = query.where(Ticker.created_at.between(date_from, date_to))
        elif date_to and not date_from:
            query = query.where(Ticker.created_at <= date_to)
        elif date_from and not date_to:
            query = query.where(Ticker.created_at >= date_from)
        result = await self.session.execute(query)
        return result.scalars().all()
