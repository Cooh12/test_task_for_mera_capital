from datetime import datetime
from typing import TypeVar, Type, Generic, Sequence

from sqlalchemy import delete, func, ScalarResult
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.interfaces import ORMOption

from app.infrastructure.db.models import BaseModel

Model = TypeVar("Model", bound=BaseModel, covariant=True, contravariant=False)


class BaseDAO(Generic[Model]):
    def __init__(self, model: Type[Model], session: AsyncSession):
        self.model = model
        self.session = session

    async def _get_all(self, options: Sequence[ORMOption] = tuple()) -> Sequence[Model]:
        result: ScalarResult[Model] = await self.session.scalars(
            select(self.model).options(*options)
        )
        return result.all()

    async def _get_by_id(
            self, id_: int, options: Sequence[ORMOption] = None, populate_existing: bool = False
    ) -> Model:
        result = await self.session.get(
            self.model, id_, options=options, populate_existing=populate_existing
        )
        if result is None:
            raise NoResultFound()
        return result

    def _save(self, obj: BaseModel):
        self.session.add(obj)

    async def delete_all(self):
        await self.session.execute(delete(self.model))

    async def _delete(self, obj: BaseModel):
        await self.session.delete(obj)

    async def count(self):
        result = await self.session.execute(select(func.count(self.model.id)))
        return result.scalar_one()

    async def commit(self):
        await self.session.commit()

    async def _flush(self, *objects: BaseModel):
        await self.session.flush(objects)

    async def get_curent_price(self):
        result = await self.session.execute(select(self.model).order_by(self.model.id.desc()).limit(1))
        return result.scalar_one()

    async def get_all_values(self, date_from: int | None, date_to: int | None):
        if not date_from:
            date_from = 1686420252
        if not date_to:
            date_to = float(datetime.now().timestamp())
        query = select(self.model).where(self.model.current_time.between(date_from, date_to))
        result = await self.session.execute(query)
        return result.scalars().all()
