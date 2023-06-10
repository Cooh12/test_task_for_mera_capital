from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from ...models import BTC


class BTCDAO(BaseDAO[BTC]):
    def __init__(self, session: AsyncSession):
        super().__init__(BTC, session)

    # async def curent_price(self):
    #     result = await self.session.execute(select(BTC).order_by(BTC.id.desc()).limit(1))
    #     return result.scalar_one()
