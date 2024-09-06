from pydantic import ConfigDict

from src.schemas import BaseSchema


class TextStat(BaseSchema):
    complexity: dict

    model_config = ConfigDict(from_attributes=True)
