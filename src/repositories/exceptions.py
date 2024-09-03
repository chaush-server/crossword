from fastapi.exceptions import HTTPException


class BaseError(HTTPException):
    status_code: int
    detail: str


class NotFoundError(BaseError):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)


class ServerError(BaseError):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)
