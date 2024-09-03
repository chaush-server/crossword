import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.api.routes import routers
from src.repositories.exception_handlers import exception_handlers


def create_app() -> FastAPI:
    app = FastAPI(title="Crossword", description="Crossword API")

    @app.get("/")
    async def redirect() -> RedirectResponse:
        return RedirectResponse(url="/docs")

    for router in routers:
        app.include_router(router)

    for exception, handler in exception_handlers.items():
        app.add_exception_handler(
            exc_class_or_status_code=exception,
            handler=handler,
        )

    return app


if __name__ == "__main__":
    uvicorn.run(app="src:create_app", reload=True)
