from typing import TYPE_CHECKING, List

from src.enums import Direction
from src.schemas import BaseSchema

if TYPE_CHECKING:
    from src.repositories.db.models import LevelWord


class LevelCharSchema(BaseSchema):
    char: str
    x: int
    y: int

    @classmethod
    def get_chars_from_word(cls, word: "LevelWord") -> List["LevelCharSchema"]:
        chars = []
        for i, char in enumerate(word.word):
            x = word.x
            y = word.y
            if word.direction == Direction.H:
                x += i
            else:
                y += i
            chars.append(LevelCharSchema(char=char, x=x, y=y))
        return chars
