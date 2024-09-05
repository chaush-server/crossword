from src.repositories.apis.crossmaker.repositories import CrossMakerRepository


class CrossMakerService:
    def __init__(self, cross_maker_repo: CrossMakerRepository):
        self.cross_maker_repo: CrossMakerRepository = cross_maker_repo

    async def make_crossword(self, words):
        return await self.cross_maker_repo.make_crossword(words)


