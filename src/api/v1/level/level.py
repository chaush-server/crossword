from typing import Annotated, List

from fastapi import APIRouter, Depends

from src.api.dependencies import (
    provide_cross_maker_service, provide_level_service,
)
from src.schemas.level import Level
from src.services.cross_maker import CrossMakerService
from src.services.level import LevelService

level_router = APIRouter(prefix="/levels", tags=["Levels"])


@level_router.post("/generate/", response_model=Level)
async def generate_level(
    cross_maker_service: Annotated[
        CrossMakerService,
        Depends(provide_cross_maker_service),
    ],
    level_service: Annotated[
        LevelService,
        Depends(provide_level_service),
    ],
    words: List[str],
    size: int = 25,
) -> Level:
    cross = await cross_maker_service.make_crossword(words, size)
    level = level_service.level_from_cross(cross)
    return level
