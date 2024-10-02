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
    def from_word(cls, word: "LevelWord") -> List["LevelCharSchema"]:
        return cls.from_str_and_direction(
            word=word.word,
            x=word.x,
            y=word.y,
            direction=word.direction,
        )

    @classmethod
    def from_str_and_direction(
        cls, word: str, x: int, y: int, direction: Direction
    ) -> List["LevelCharSchema"]:
        chars = []
        for char in word:
            chars.append(cls(char=char, x=x, y=y))
            if direction == Direction.H:
                x += 1
            elif direction == Direction.V:
                y += 1

        return chars
