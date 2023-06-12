from datetime import datetime
from enum import Enum

from app.core.models import dto
from app.infrastructure.db.dao.holder import HolderDao


class CoinName(str, Enum):
    BTC = "btc"
    ETH = "eth"


async def get_current_price(dao: HolderDao, coin_name: CoinName) -> dto.Coin:
    result = await dao.coin.get_curent_price(coin_name.value)
    return result.to_dto


async def get_all_values(dao: HolderDao, coin_name: CoinName, date_from: datetime, date_to: datetime) -> list[dto.Coin]:
    if date_from:
        date_from = float(date_from.timestamp())
    if date_to:
        date_to = float(date_to.timestamp())
    result = await dao.coin.get_all_values(coin_name.value, date_from, date_to)
    return [value.to_dto for value in result]
