from typing import Annotated

from fastapi import Depends
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import Config
from src.repositories.apis.crossmaker.repositories import CrossMakerRepository
from src.repositories.db import get_async_session
from src.repositories.db.repositories import LevelRepository, WordRepository
from src.services.analyzer import AnalyzerService
from src.services.cross_maker import CrossMakerService
from src.services.level import LevelService
from src.services.word import WordService


async def provide_level_service(
    session: Annotated[AsyncSession, Depends(get_async_session)]
) -> LevelService:
    return LevelService(LevelRepository(session))


async def provide_analyzer_service() -> AnalyzerService:
    return AnalyzerService()


async def provide_cross_maker_service() -> CrossMakerService:
    return CrossMakerService(
        CrossMakerRepository(client=AsyncClient(base_url=Config.CROSSMAKER_BASE_URL))
    )


async def provide_word_service(
    session: Annotated[AsyncSession, Depends(get_async_session)]
) -> WordService:
    return WordService(WordRepository(session))
