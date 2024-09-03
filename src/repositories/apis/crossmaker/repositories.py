from abc import ABC, abstractmethod
from typing import Sequence

from httpx import AsyncClient


class CrossMakerRepositoryInterface(ABC):
    @abstractmethod
    async def make_crossword(self, words: Sequence[str]) -> str: ...


class CrossMakerRepository(CrossMakerRepositoryInterface):
    def __init__(self, client: AsyncClient):
        self.client = client

    async def make_crossword(self, words: Sequence[str]) -> str:
        return "crossword"
