from sqlalchemy import Numeric, Text, BigInteger
from sqlalchemy.orm import mapped_column, Mapped

from app.core.models import dto
from .base import BaseModel


class Ticker(BaseModel):
    __tablename__ = 'tickers'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    coin_name: Mapped[str] = mapped_column(Text)
    estimated_delivery_price: Mapped[float] = mapped_column(Numeric)
    index_price: Mapped[float] = mapped_column(Numeric)
    created_at: Mapped[float] = mapped_column(Numeric)

    @property
    def to_dto(self):
        return dto.Ticker(
            coin_name=self.coin_name,
            estimated_delivery_price=self.estimated_delivery_price,
            index_price=self.index_price,
            created_at=self.created_at
        )
