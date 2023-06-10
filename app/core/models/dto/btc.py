from dataclasses import dataclass
from datetime import datetime

from app.infrastructure.db import models as db_models


@dataclass
class BTC:
    estimated_delivery_price: float
    index_price: float
    current_time: float = float(datetime.now().timestamp())

    @property
    def to_db(self):
        return db_models.BTC(
            estimated_delivery_price=self.estimated_delivery_price,
            index_price=self.index_price,
            current_time=self.current_time
        )
