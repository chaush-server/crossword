from typing import Optional

from pydantic import BaseModel

from src.enums import Direction


class WordSchema(BaseModel):
    id: int
    word: str
    translate: Optional[str]
    direction: Direction
    x: int
    y: int

    class Config:
        from_attributes = True
