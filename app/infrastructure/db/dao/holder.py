from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.dao.rdb import CoinDAO


class HolderDao:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.coin = CoinDAO(self.session)
