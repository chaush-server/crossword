from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.repositories.db.models.base import Base
from src.repositories.db.models.level_word import LevelWord
from src.schemas.level import LevelSchema


class Level(Base):
    __tablename__ = "level"

    id: Mapped[int] = mapped_column(primary_key=True)
    chars: Mapped[str] = mapped_column()

    words: Mapped[List[LevelWord]] = relationship(back_populates="level", lazy="selectin")

    def to_read_model(self) -> LevelSchema:
        words = [word.to_read_model() for word in self.words]
        return LevelSchema(
            id=self.id,
            chars=self.chars,
            words=words,
        )
