from pydantic import BaseModel


class TextSchema(BaseModel):
    text: str

    class Config:
        from_attributes = True
