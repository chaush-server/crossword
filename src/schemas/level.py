from typing import List

from pydantic import BaseModel

from src.schemas.word import LevelWordSchema


class LevelSchema(BaseModel):
    id: int
    chars: str
    words: List[LevelWordSchema]

    class Config:
        from_attributes = True
