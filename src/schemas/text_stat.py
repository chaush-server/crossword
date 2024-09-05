from pydantic import BaseModel


class TextStat(BaseModel):
    complexity: dict

    class Config:
        from_attributes = True
