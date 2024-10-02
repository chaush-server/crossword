from pydantic import ConfigDict

from src.schemas import BaseSchema


class TextStat(BaseSchema):
    complexity: dict[str, float]

    model_config = ConfigDict(from_attributes=True)
