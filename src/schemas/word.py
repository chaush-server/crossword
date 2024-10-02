from typing import Optional, List

from src.schemas import BaseSchema
from src.schemas.char import LevelCharSchema


class LevelWordSchema(BaseSchema):
    id: int
    word: str
    translate: Optional[str]
    chars: List[LevelCharSchema]
