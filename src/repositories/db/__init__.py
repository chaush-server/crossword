from typing import (
    Type,
    Sequence,
    TypeVar,
    Generic,
    Optional,
    AsyncGenerator,
    Dict,
    Any,
)

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from abc import ABC, abstractmethod

from sqlalchemy import select

from src.config import Config
from src.repositories.db.models.base import Base
from src.repositories.exceptions import NotFoundError

engine = create_async_engine(Config.DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


T = TypeVar("T", bound=Base)


class AbstractRepository(ABC, Generic[T]):
    @abstractmethod
    async def get_by_id(self, model_id: int) -> T: ...

    @abstractmethod
    async def get_all(self, limit: int, offset: int) -> Sequence[T]: ...

    @abstractmethod
    async def add_one(self, data: Dict[str, Any]) -> None: ...


class SQLAlchemyRepository(AbstractRepository[T]):
    def __init__(self, model: Type[T], session: AsyncSession):
        self.model = model
        self.session = session

    async def get_by_id(self, model_id: int) -> T:
        res: Optional[T] = await self.session.get(self.model, model_id)
        if not res:
            raise NotFoundError(
                detail=f"{self.model.__name__} with id {model_id} not found"
            )
        return res

    async def get_all(self, limit: int = 10, offset: int = 0) -> Sequence[T]:
        query = await self.session.execute(
            select(self.model).limit(limit).offset(offset)
        )
        result = query.scalars().all()
        if not result:
            raise NotFoundError(detail=f"{self.model.__name__}'s not found")
        return result

    async def add_one(self, data: Dict[str, Any]) -> None:
        self.session.add(self.model(**data))
