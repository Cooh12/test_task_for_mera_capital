from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.dao.rdb import BTCDAO, ETHDAO


class HolderDao:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.btc = BTCDAO(self.session)
        self.eth = ETHDAO(self.session)
