from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from ...models import Coin


class CoinDAO(BaseDAO[Coin]):
    def __init__(self, session: AsyncSession):
        super().__init__(Coin, session)

    async def get_curent_price(self, coin_name: str) -> Coin:
        result = await self.session.execute(
            select(Coin).where(Coin.coin_name == coin_name).order_by(Coin.id.desc()).limit(1))
        return result.scalar_one()

    async def get_all_values(self, coin_name: str, date_from: float | None, date_to: float | None) -> list[Coin]:
        query = select(Coin).where(Coin.coin_name == coin_name)
        print(date_from, date_to)
        if date_from and date_to:
            query = query.where(Coin.created_at.between(date_from, date_to))
        elif date_to and not date_from:
            query = query.where(Coin.created_at <= date_to)
        elif date_from and not date_to:
            query = query.where(Coin.created_at >= date_from)
        result = await self.session.execute(query)
        return result.scalars().all()
