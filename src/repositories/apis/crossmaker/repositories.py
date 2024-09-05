from abc import ABC, abstractmethod
from typing import Sequence

from httpx import AsyncClient

from src.config import Config
from src.repositories.exceptions import ServerError


class CrossMakerRepositoryInterface(ABC):
    @abstractmethod
    async def make_crossword(self, words: Sequence[str]) -> str: ...


class CrossMakerRepository(CrossMakerRepositoryInterface):
    def __init__(self, client: AsyncClient):
        self.client = client
        self.url = Config.CROSSMAKER_URL

    async def make_crossword(self, words: Sequence[str]) -> str:
        await self.client.get("https://crossmaker.ru/ru/")
        r = await self.client.put(url=self.url, json={"size": 25, "words": words})
        if r.status_code != 200:
            raise ServerError(r.text)
        return r.json().get("cross")
