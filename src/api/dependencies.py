from httpx import AsyncClient

from src.repositories.apis.crossmaker.repositories import CrossMakerRepository
from src.services.analyzer import AnalyzerService
from src.services.cross_maker import CrossMakerService
from src.services.level import LevelService


async def provide_analyzer_service() -> AnalyzerService:
    return AnalyzerService()


async def provide_cross_maker_service() -> CrossMakerService:
    return CrossMakerService(
        CrossMakerRepository(client=AsyncClient())
    )


async def provide_level_service() -> LevelService:
    return LevelService()

