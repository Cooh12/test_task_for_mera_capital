from datetime import datetime

from adaptix import Retort
from fastapi import APIRouter, Depends

from app.core.interfaces.db_provaider_protocol import dao
from app.core.models import dto
from app.core.models.enums.tickers import Ticker
from app.core.services.query import get_current_price, get_all_values
from app.infrastructure.db.dao.holder import HolderDao

rerort = Retort()

coins_router = APIRouter(
    prefix="/coins",
    tags=["coins"]
)


@coins_router.get('/current_price')
async def read_current_price(ticker: Ticker,
                             dao: HolderDao = Depends(dao)) -> dto.Ticker:
    return await get_current_price(dao, ticker)


@coins_router.get('/all_values')
async def read_all_values(tiker: Ticker, date_from: datetime | None = None, date_to: datetime | None = None,
                          dao: HolderDao = Depends(dao)) -> list[dto.Ticker]:
    return await get_all_values(dao, tiker, date_from, date_to)
