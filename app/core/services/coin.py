from datetime import datetime, date
from enum import Enum

from app.infrastructure.db.dao.holder import HolderDao


class Ticker(str, Enum):
    BTC = "btc"
    ETH = "eth"


async def get_current_price(dao: HolderDao, ticker: Ticker):
    if ticker == Ticker.BTC:
        result = await dao.btc.get_curent_price()
        return result.to_dto
    elif ticker == Ticker.ETH:
        result = await dao.eth.get_curent_price()
        return result.to_dto


async def get_all_values(dao: HolderDao, ticker: str, date_from: date, date_to: date):
    if date_from:
        date_from = int(datetime.strptime(str(date_from), "%Y-%m-%d").timestamp())
    if date_to:
        date_to = int(datetime.strptime(str(date_to), "%Y-%m-%d").timestamp())
    if ticker == Ticker.BTC:
        result = await dao.btc.get_all_values(date_from, date_to)
        return [value.to_dto for value in result]
    elif ticker == Ticker.ETH:
        result = await dao.eth.get_all_values(date_from, date_to)
        return [value.to_dto for value in result]
