import json

import pytest
from aiohttp import web


async def previous(request):
    response = {
        "jsonrpc": "2.0",
        "result": {
            "estimated_delivery_price": 11628.81,
            "index_price": 11628.81
        }
    }
    my_list_str = json.dumps(response)
    return web.Response(text=my_list_str, content_type="application/json")


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    app.router.add_get('get_index_price', previous)
    return loop.run_until_complete(aiohttp_client(app))