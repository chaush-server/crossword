from typing import Any, Callable, Coroutine

from fastapi import Request
from fastapi.responses import JSONResponse

from src.repositories.exceptions import NotFoundError, BaseError


def not_found_handler(request: Request, exception: NotFoundError) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code,
        content={"detail": exception.detail},
    )


def exception_handler(request: Request, exception: BaseError) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code,
        content={"detail": str(exception)},
    )


exception_handlers: dict[type[Exception], Callable[[Request, Any], JSONResponse]] = {
    BaseError: exception_handler,
    NotFoundError: not_found_handler,
}
