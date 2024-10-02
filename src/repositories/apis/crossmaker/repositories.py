from abc import ABC, abstractmethod
from typing import Sequence, Any, Dict, List

from httpx import AsyncClient

from src.config import Config
from src.repositories.exceptions import ServerError


class CrossMakerRepositoryInterface(ABC):
    @abstractmethod
    async def make_crossword(self, words: Sequence[str]) -> List[Dict[str, Any]]: ...


class CrossMakerRepository(CrossMakerRepositoryInterface):
    def __init__(self, client: AsyncClient):
        self.client = client

    async def make_crossword(self, words: Sequence[str]) -> List[Dict[str, Any]]:
        r = await self.client.put(
            url=Config.CROSSMAKER_URL, json={"size": 25, "words": words}
        )
        if r.status_code != 200:
            raise ServerError(r.text)

        cross = r.json().get("cross")
        if not isinstance(cross, list):
            raise ServerError(r.text)

        return cross
