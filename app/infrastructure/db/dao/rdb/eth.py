from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from ...models import ETH


class ETHDAO(BaseDAO[ETH]):
    def __init__(self, session: AsyncSession):
        super().__init__(ETH, session)
