from typing import Annotated, List

from fastapi import APIRouter, Depends

from src.api.dependencies import (
    provide_level_service,
    provide_cross_maker_service,
    provide_word_service,
)
from src.schemas.level import LevelSchema
from src.schemas.word import LevelWordSchema
from src.services.cross_maker import CrossMakerService
from src.services.level import LevelService
from src.services.word import WordService

level_router = APIRouter(prefix="/levels", tags=["Levels"])


@level_router.get("", response_model=List[LevelSchema])
async def get_levels(
    level_service: Annotated[
        LevelService,
        Depends(provide_level_service),
    ],
) -> List[LevelSchema]:
    levels = await level_service.get_levels()
    return levels


@level_router.get("/{level_id}", response_model=LevelSchema)
async def get_level(
    level_id: int,
    level_service: Annotated[
        LevelService,
        Depends(provide_level_service),
    ],
) -> LevelSchema:
    level = await level_service.get_level(level_id)
    return level


@level_router.post("/generate/{difficulty}", response_model=LevelSchema)
async def generate_level(
    difficulty: int,
    cross_maker_service: Annotated[
        CrossMakerService,
        Depends(provide_cross_maker_service),
    ],
    word_service: Annotated[
        WordService,
        Depends(provide_word_service),
    ],
) -> LevelSchema:
    words = await word_service.get_random_words(word_count=10, max_unique_chars=10)
    chars = await word_service.get_unique_chars(words)
    stringify_words = await word_service.stringify_words(words)
    cross = await cross_maker_service.make_crossword(stringify_words)
    level_words = LevelWordSchema.from_cross(cross)
    return LevelSchema(id=0, chars=chars, words=level_words)
