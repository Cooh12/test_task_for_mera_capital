from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.dao.rdb.ticker import TickerDAO


class HolderDao:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.ticker = TickerDAO(self.session)
