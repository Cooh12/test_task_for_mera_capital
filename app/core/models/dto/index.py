from dataclasses import dataclass
from datetime import datetime

from app.infrastructure.db import models as db_models


@dataclass
class Coin:
    coin_name: str
    estimated_delivery_price: float
    index_price: float
    created_at: float = float(datetime.now().timestamp())

    @property
    def to_db(self):
        return db_models.Coin(
            coin_name=self.coin_name,
            estimated_delivery_price=self.estimated_delivery_price,
            index_price=self.index_price,
            created_at=self.created_at
        )
