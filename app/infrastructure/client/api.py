from adaptix import Retort, name_mapping

from app.core.interfaces.client_protocol import DeribitProtocol
from app.core.models import dto
from app.infrastructure.client.base_client import BaseClient
from app.infrastructure.client.urls import Urls


class DeribitClient(BaseClient, DeribitProtocol):
    url = Urls()
    _retort = Retort(recipe=[
        name_mapping(dto.Coin, map=[{
            "coin_name": "coin_name",
            "index_price": ("model", "index_price"),
            "estimated_delivery_price": ("model", "estimated_delivery_price"),
        }, (".*", ("model", ...))])
    ])

    def __init__(self):
        super().__init__(session=self.create_session())

    async def get_index_price(self, ticker: str) -> dto.Coin:
        url = self.url.GET_INDEX_PRICE.format(ticker)
        response = await self._get(url)
        return self._retort.load({"coin_name": ticker.split('_')[0], "model": response.get('result')}, dto.Coin)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.close()
