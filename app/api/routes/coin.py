from datetime import datetime

from adaptix import Retort
from fastapi import APIRouter, Depends

from app.core.interfaces.db_provaider_protocol import dao
from app.core.models import dto
from app.core.services.coin import get_current_price, CoinName, get_all_values
from app.infrastructure.db.dao.holder import HolderDao

rerort = Retort()

coins_router = APIRouter(
    prefix="/coins",
    tags=["coins"]
)


@coins_router.get('/current_price')
async def read_current_price(coin_name: CoinName,
                             dao: HolderDao = Depends(dao)) -> dto.Coin:
    return await get_current_price(dao, coin_name)


@coins_router.get('/all_values')
async def read_all_values(coin_name: CoinName, date_from: datetime | None = None, date_to: datetime | None = None,
                          dao: HolderDao = Depends(dao)) -> list[dto.Coin]:
    return await get_all_values(dao, coin_name, date_from, date_to)
