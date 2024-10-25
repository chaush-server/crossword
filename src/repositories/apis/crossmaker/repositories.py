from typing import Sequence, Any, Dict

from httpx import AsyncClient

from src.config import Config
from src.repositories.exceptions import ServerError


class CrossMakerRepository:
    def __init__(self, client: AsyncClient):
        self.client = client

    async def make_crossword(self, words: Sequence[str], size: int) -> Dict[str, Any]:
        r = await self.client.put(
            url=Config.CROSSMAKER_URL, json={"size": size, "words": words}
        )
        if r.status_code != 200:
            raise ServerError(r.text)

        cross: Dict[str, Any] = r.json()
        if not cross or not cross["ok"]:
            raise ServerError(r.text)

        return cross
