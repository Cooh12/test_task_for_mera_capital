from fastapi import FastAPI

from app.api.routes.coin import coins_router
from app.api.routes.default import default_router
from app.api.routes.healthcheck import healthcheck_router


def setup_routes(app: FastAPI) -> None:
    app.include_router(default_router)
    app.include_router(healthcheck_router)
    app.include_router(coins_router)
