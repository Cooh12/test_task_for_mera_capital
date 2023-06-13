from adaptix import Retort, name_mapping

from app.core.interfaces.client_protocol import DeribitProtocol
from app.core.models import dto


class DeribitClientMock(DeribitProtocol):
    _retort = Retort(recipe=[
        name_mapping(dto.Ticker, map=[{
            "coin_name": "coin_name",
            "index_price": ("model", "index_price"),
            "estimated_delivery_price": ("model", "estimated_delivery_price"),
        }, (".*", ("model", ...))])
    ])

    async def get_index_price(self, ticker: str, response: dict) -> dto.Ticker:
        return self._retort.load({"coin_name": ticker, "model": response.get('result')}, dto.Ticker)
