from adaptix import Retort

from app.core.interfaces.client_protocol import DeribitProtocol
from app.core.models import dto
from app.infrastructure.client.base_client import BaseClient
from app.infrastructure.client.urls import Urls


class DeribitClient(BaseClient, DeribitProtocol):
    url = Urls()
    _retort = Retort()

    def __init__(self):
        super().__init__(session=self.create_session())

    async def get_index_price_for_btc(self) -> dto.BTC:
        url = self.url.GET_INDEX_PRICE.format('btc_usd')
        response = await self._get(url)
        return self._retort.load(response.get('result'), dto.BTC)

    async def get_index_price_for_eth(self) -> dto.ETH:
        url = self.url.GET_INDEX_PRICE.format('eth_usd')
        response = await self._get(url)
        return self._retort.load(response.get('result'), dto.ETH)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.close()
