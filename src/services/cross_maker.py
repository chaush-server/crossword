from typing import Sequence, Dict, Any

from src.repositories.apis.crossmaker.repositories import CrossMakerRepository


class CrossMakerService:
    def __init__(self, cross_maker_repo: CrossMakerRepository):
        self.cross_maker_repo: CrossMakerRepository = cross_maker_repo

    async def make_crossword(self, words: Sequence[str], size: int) -> Dict[str, Any]:
        return await self.cross_maker_repo.make_crossword(words, size)
