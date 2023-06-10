from typing import Protocol

from app.core.models import dto


class DeribitProtocol(Protocol):
    async def get_index_price_for_btc(self) -> dto.BTC:
        raise NotImplementedError

    async def get_index_price_for_eth(self) -> dto.ETH:
        raise NotImplementedError
