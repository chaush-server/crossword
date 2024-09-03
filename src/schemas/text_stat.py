from pydantic import BaseModel


class TextStat(BaseModel):
    complexity: float

    class Config:
        from_attributes = True
