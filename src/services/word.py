from typing import Sequence

from src.repositories.db.models import Word
from src.repositories.db.repositories import WordRepository


class WordService:
    def __init__(self, word_repo: WordRepository):
        self.word_repo: WordRepository = word_repo

    async def get_random_words(
        self, word_count: int = 10, max_unique_chars: int = 6
    ) -> Sequence[Word]:
        return await self.word_repo.get_random_words(word_count, max_unique_chars)

    async def get_unique_chars(self, words: Sequence[Word]) -> str:
        return await self.get_chars_from_words(words)

    @staticmethod
    async def get_chars_from_words(words: Sequence[Word]) -> str:
        chars = set()
        for word in words:
            for i in word.word:
                chars.add(i)
        return "".join(chars)

    @staticmethod
    async def stringify_words(words: Sequence[Word]) -> Sequence[str]:
        return [item.word for item in words]
