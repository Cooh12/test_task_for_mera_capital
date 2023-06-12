from datetime import datetime
from enum import Enum

from app.core.models import dto
from app.core.models.enums.tickers import Ticker
from app.infrastructure.db.dao.holder import HolderDao


class CoinName(str, Enum):
    BTC = "btc"
    ETH = "eth"


async def get_current_price(dao: HolderDao, ticker: Ticker) -> dto.Ticker:
    result = await dao.ticker.get_curent_price(ticker.value)
    return result.to_dto


async def get_all_values(dao: HolderDao, ticker: Ticker, date_from: datetime, date_to: datetime) -> list[dto.Ticker]:
    if date_from:
        date_from = float(date_from.timestamp())
    if date_to:
        date_to = float(date_to.timestamp())
    result = await dao.ticker.get_all_values(ticker.value, date_from, date_to)
    return [value.to_dto for value in result]
