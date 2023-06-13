import datetime
import json
import logging

from aiohttp import web

from app.core.models import dto
from tests.mocks.client_mocks import DeribitClientMock

logger = logging.getLogger(__name__)

pytest_plugins = 'aiohttp.pytest_plugin'


async def test_get_index_price(cli, client_mock: DeribitClientMock) -> None:
    resp = await cli.get('/')
    result = dto.Ticker(coin_name='btc_usd', estimated_delivery_price=26319.64, index_price=26319.64,
                        created_at=float(datetime.datetime.now().timestamp()))
    assert result == await client_mock.get_index_price('btc_usd', await resp.json())


async def func(request):
    my_list_str = json.dumps()
    return web.Response(text=my_list_str, content_type="application/json")
