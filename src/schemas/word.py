from typing import Optional

from src.enums import Direction
from src.schemas import BaseSchema


class LevelWordSchema(BaseSchema):
    id: int
    word: str
    translate: Optional[str]
    direction: Direction
    x: int
    y: int
