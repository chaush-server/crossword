from typing import Annotated, List

from fastapi import APIRouter, Depends

from src.schemas.level import LevelSchema
from src.api.dependencies import (
    provide_level_service,
    provide_cross_maker_service,
    provide_word_service,
)
from src.services.cross_maker import CrossMakerService
from src.services.level import LevelService
from src.services.word import WordService

level_router = APIRouter(prefix="/levels", tags=["Levels"])


@level_router.get("", response_model=List[LevelSchema])
async def get_levels(
    level_service: Annotated[LevelService, Depends(provide_level_service)]
) -> List[LevelSchema]:
    levels = await level_service.get_levels()
    return levels


@level_router.get("/{level_id}", response_model=LevelSchema)
async def get_level(
    level_id: int,
    level_service: Annotated[LevelService, Depends(provide_level_service)],
) -> LevelSchema:
    level = await level_service.get_level(level_id)
    return level


@level_router.post("/generate/{difficulty}")
async def generate_level(
    difficulty: int,
    cross_maker_service: Annotated[
        CrossMakerService, Depends(provide_cross_maker_service)
    ],
    word_service: Annotated[WordService, Depends(provide_word_service)],
):
    if difficulty < 2:
        words = await word_service.get_random_words(word_count=10, max_unique_chars=10)
        words = [word.word for word in words]
        chars = set()
        for word in words:
            for i in word:
                chars.add(i)
        print(chars)
        print(len(chars))
    else:
        words = ["тест1", "тест2", "тест3", "тест4", "тест5"]
    return await cross_maker_service.make_crossword(words)
