from typing import List

from src.repositories.db.repositories import LevelRepository
from src.schemas.level import LevelSchema


class LevelService:
    def __init__(self, level_repo: LevelRepository):
        self.level_repo: LevelRepository = level_repo

    async def get_level(self, level_id: int) -> LevelSchema:
        level = await self.level_repo.get_by_id(level_id)
        return level.to_read_model()

    async def get_levels(self) -> List[LevelSchema]:
        levels = await self.level_repo.get_all()
        return [level.to_read_model() for level in levels]
