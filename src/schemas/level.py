from typing import List

from pydantic import BaseModel, ConfigDict

from src.schemas.word import LevelWordSchema


class LevelSchema(BaseModel):
    id: int
    chars: str
    words: List[LevelWordSchema]

    model_config = ConfigDict(from_attributes=True)
