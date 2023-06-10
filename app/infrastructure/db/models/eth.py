from sqlalchemy import BigInteger, Numeric
from sqlalchemy.orm import mapped_column, Mapped

from .base import BaseModel


class ETH(BaseModel):
    __tablename__ = 'eth_coin'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    estimated_delivery_price: Mapped[float] = mapped_column(Numeric)
    index_price: Mapped[float] = mapped_column(Numeric)
    current_time: Mapped[float] = mapped_column(Numeric)

    @property
    def to_dto(self):
        from app.core.models import dto
        return dto.BTC(
            estimated_delivery_price=self.estimated_delivery_price,
            index_price=self.index_price,
            current_time=self.current_time
        )
