from sqlalchemy.orm import Mapped, mapped_column

from src.repositories.db.models.base import Base


class Word(Base):
    __tablename__ = "word"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column()
    language_id: Mapped[int] = mapped_column()
    raw_translation_id: Mapped[int] = mapped_column()
