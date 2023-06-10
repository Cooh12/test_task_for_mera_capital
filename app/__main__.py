import asyncio
import logging

from sqlalchemy.orm import close_all_sessions

from app.common.config import load_config, Config
from app.common.config.logging_config import setup_logging
from app.infrastructure.api.factory import init_api, run_api
from app.infrastructure.db.factory import create_engine, create_session_maker
from app.infrastructure.scheduler import ApScheduler

logger = logging.getLogger(__name__)


async def main():
    setup_logging()
    config = load_config(Config)
    engine = create_engine(config.db)
    pool = create_session_maker(engine)
    scheduler = ApScheduler(pool)
    app = init_api(False, pool)
    try:
        await scheduler.job()
        await scheduler.start()
        await run_api(app)
    finally:
        close_all_sessions()
        await engine.dispose()
        await scheduler.close()
        logger.info("App is stopped")


if __name__ == "__main__":
    asyncio.run(main())
