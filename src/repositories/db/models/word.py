from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import Direction
from src.repositories.db.models.base import Base
from src.schemas.word import WordSchema

if TYPE_CHECKING:
    from src.repositories.db.models import Level


class Word(Base):
    __tablename__ = "word"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column()
    x: Mapped[int] = mapped_column()
    y: Mapped[int] = mapped_column()
    direction: Mapped[Direction] = mapped_column()
    translate: Mapped[str] = mapped_column(nullable=True)
    level_id: Mapped[int] = mapped_column(ForeignKey("level.id"), nullable=False)

    level: Mapped["Level"] = relationship("Level", back_populates="words")

    def to_read_model(self) -> WordSchema:
        return WordSchema(
            id=self.id,
            word=self.word,
            translate=self.translate,
            direction=self.direction,
            x=self.x,
            y=self.y,
        )
