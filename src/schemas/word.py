from typing import List

from src.schemas import BaseSchema
from src.schemas.char import Char


class Word(BaseSchema):
    word: str
    chars: List[Char]
