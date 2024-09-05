from typing import Annotated

from fastapi import Depends
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.apis.crossmaker.repositories import CrossMakerRepository
from src.repositories.db import get_async_session
from src.repositories.db.repositories import LevelRepository
from src.services.analyzer import AnalyzerService
from src.services.cross_maker import CrossMakerService
from src.services.level import LevelService


async def provide_level_service(
    session: Annotated[AsyncSession, Depends(get_async_session)]
) -> LevelService:
    return LevelService(LevelRepository(session))


async def provide_analyzer_service() -> AnalyzerService:
    return AnalyzerService()


async def provide_cross_maker_service(
) -> CrossMakerService:
    return CrossMakerService(CrossMakerRepository(AsyncClient()))
