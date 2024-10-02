from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import provide_analyzer_service
from src.schemas.text import TextSchema
from src.schemas.text_stat import TextStat
from src.services.analyzer import AnalyzerService

text_router = APIRouter(prefix="/texts", tags=["Texts"])


@text_router.post("/complexity", response_model=TextStat)
async def complexity(
    text: TextSchema,
    text_service: Annotated[
        AnalyzerService,
        Depends(provide_analyzer_service),
    ],
) -> TextStat:
    text_complexity = await text_service.get_text_complexity(text.text)
    return TextStat(complexity=text_complexity)
