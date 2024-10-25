from typing import Dict, Any

from src.enums import Direction
from src.schemas.char import Char
from src.schemas.level import Level
from src.schemas.word import Word


class LevelService:
    @staticmethod
    def get_char_from_attrs(i: int, char: str, x: int, y: int, direction: str) -> Char:
        if direction == Direction.H:
            x += i
        elif direction == Direction.V:
            y += i
        return Char(char=char, x=x, y=y)

    @classmethod
    def word_from_cross(cls, word: Dict[str, Any]) -> Word:
        chars = []
        for i, char in enumerate(word["word"]):
            chars.append(
                cls.get_char_from_attrs(
                    char=char, x=word["x"], y=word["y"], i=i, direction=word["direction"]
                )
            )

        return Word(
            word=word["word"],
            chars=chars,
        )

    @classmethod
    def level_from_cross(cls, cross: Dict[str, Any]) -> Level:
        chars = list(set("".join(cross["words_used"])))
        return Level(
            size=cross["size"],
            chars=chars,
            words=[cls.word_from_cross(word) for word in cross["cross"]],
        )
