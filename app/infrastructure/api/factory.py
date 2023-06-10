import logging

import uvicorn as uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.infrastructure.api import setup_routes
from app.infrastructure.api.providers import setup_providers

logger = logging.getLogger(__name__)


def init_api(debug: bool, pool: async_sessionmaker) -> FastAPI:
    logger.debug("Initialize API")
    app = FastAPI(debug=debug, title="Test_task_MERA-CAPITAL", version="0.1b")
    setup_providers(app, pool)
    setup_routes(app)
    return app


async def run_api(app: FastAPI) -> None:
    config = uvicorn.Config(app, log_level=logging.INFO, log_config=None)
    server = uvicorn.Server(config)
    logger.info("Running API")
    await server.serve()
