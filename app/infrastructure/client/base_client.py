from typing import Any, TypeAlias

from aiohttp import ClientSession
from aiohttp.typedefs import StrOrURL

JsonData: TypeAlias = dict[str, Any]


class BaseClient:
    def __init__(self, session: ClientSession) -> None:
        self._session: ClientSession = session

    async def _get(self, url: StrOrURL, headers: JsonData | None = None) -> JsonData:
        session = self._get_session()
        async with session.get(url, headers=headers) as request:
            response = await request.json(content_type="application/json")
        if request.status != 200:
            raise Exception(response)
        return response

    async def _post(self, url: StrOrURL, data: JsonData, headers: JsonData | None = None) -> JsonData:
        session = self._get_session()
        async with session.post(url, data=data, headers=headers) as request:
            response = await request.json(content_type="application/json")
        if request.status != 200:
            raise Exception(response)
        return response

    def _get_session(self) -> ClientSession:
        if isinstance(self._session, ClientSession) and not self._session.closed:
            return self._session
        self._session = self.create_session(self._session.headers)
        return self._session

    @staticmethod
    def create_session() -> ClientSession:
        return ClientSession(headers={'Content-Type': 'application/json'})
