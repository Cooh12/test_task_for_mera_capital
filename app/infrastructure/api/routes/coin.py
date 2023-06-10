from datetime import date

from adaptix import Retort
from fastapi import APIRouter, Depends

from app.core.interfaces.db_provaider_protocol import dao
from app.core.models import dto
from app.core.services.coin import get_current_price, get_all_values, Ticker
from app.infrastructure.db.dao.holder import HolderDao

rerort = Retort()

coins_router = APIRouter(
    prefix="/coins",
    tags=["coins"]
)


@coins_router.get('/current_price')
async def read_current_price(ticker: Ticker,
                             dao: HolderDao = Depends(dao)) -> dto.BTC:
    return await get_current_price(dao, ticker)


@coins_router.get('/all_values')
async def read_all_values(ticker: Ticker, date_from: date | None = None, date_to: date | None = None,
                          dao: HolderDao = Depends(dao)) -> list[dto.BTC]:
    return await get_all_values(dao, ticker, date_from, date_to)
