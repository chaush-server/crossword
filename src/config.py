import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URL: str = os.environ["DATABASE_URL"]
    CROSSMAKER_BASE_URL: str = os.environ["CROSSMAKER_BASE_URL"]
    CROSSMAKER_URL: str = CROSSMAKER_BASE_URL.rstrip("/") + "/api/v1/session/crossword/"
