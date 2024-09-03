from typing import List

from pydantic import BaseModel

from src.schemas.word import WordSchema


class LevelSchema(BaseModel):
    id: int
    chars: str
    words: List[WordSchema]

    class Config:
        from_attributes = True
