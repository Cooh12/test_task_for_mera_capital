from sqlalchemy import BigInteger, Numeric
from sqlalchemy.orm import mapped_column, Mapped

from app.core.models import dto
from .base import BaseModel


class BTC(BaseModel):
    __tablename__ = 'btc_coin'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    estimated_delivery_price: Mapped[float] = mapped_column(Numeric)
    index_price: Mapped[float] = mapped_column(Numeric)
    current_time: Mapped[float] = mapped_column(Numeric)

    @property
    def to_dto(self):
        return dto.BTC(
            estimated_delivery_price=self.estimated_delivery_price,
            index_price=self.index_price,
            current_time=self.current_time
        )
