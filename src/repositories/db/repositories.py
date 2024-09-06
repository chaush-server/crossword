import random
from collections import Counter
from typing import Sequence, cast, List

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.db.models import Word
from src.repositories.db.models.level import Level
from src.repositories.db import SQLAlchemyRepository


class LevelRepository(SQLAlchemyRepository[Level]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=Level, session=session)


class WordRepository(SQLAlchemyRepository[Word]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=Word, session=session)

    async def get_random_words(
        self, word_count: int, max_unique_chars: int
    ) -> Sequence[Word]:
        unique_chars = Counter()
        words = []
        # Получаем все слова из таблицы Words
        result = await self.session.execute(
            select(Word).where(Word.language_id == 1)  # type: ignore
        )
        all_words = cast(List[Word], result.scalars().all())

        random.shuffle(all_words)
        for word in all_words:
            new_chars = Counter(word.word)
            combined_chars = unique_chars.copy()
            for k, v in new_chars.items():
                combined_chars[k] = max(unique_chars[k], v)

            # Проверяем, не превышает ли количество уникальных символов 10
            if sum(combined_chars.values()) <= max_unique_chars:
                unique_chars = combined_chars
                words.append(word)

            # Если уже выбрано 10 слов, выходим из цикла
            if len(words) == word_count:
                break
        return words


def unique_char_count(column):
    return func.length(column) - func.length(
        func.replace(column, func.left(column, 1), "")
    )
