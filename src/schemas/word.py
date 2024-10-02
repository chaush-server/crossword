from typing import Optional, List, Dict, Any

from src.enums import Direction
from src.schemas import BaseSchema
from src.schemas.char import LevelCharSchema


class LevelWordSchema(BaseSchema):
    id: int
    word: str
    translate: Optional[str]
    chars: List[LevelCharSchema]

    @classmethod
    def from_cross_item(cls, cross_item: Dict[str, Any]) -> "LevelWordSchema":
        level_chars = LevelCharSchema.from_str_and_direction(
            word=cross_item["word"],
            x=cross_item["x"],
            y=cross_item["y"],
            direction=Direction(cross_item["direction"]),
        )

        return cls(id=0, word=cross_item["word"], translate=None, chars=level_chars)

    @classmethod
    def from_cross(cls, cross: List[Dict[str, Any]]) -> List["LevelWordSchema"]:
        return [cls.from_cross_item(item) for item in cross]
