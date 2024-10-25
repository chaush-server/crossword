from typing import List

from pydantic import BaseModel

from src.schemas.word import Word


class Level(BaseModel):
    size: int
    chars: List[str]
    words: List[Word]

