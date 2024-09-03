from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.db.models.level import Level
from src.repositories.db import SQLAlchemyRepository


class LevelRepository(SQLAlchemyRepository[Level]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=Level, session=session)
