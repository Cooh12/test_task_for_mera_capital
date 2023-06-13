import logging.config
import os
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

DEFAULT_CONFIG_PATH = Path(__file__).parent.parent.parent.parent / "config/logging.yml"


def setup_logging(path: str | None = None):
    if path is None:
        path = os.getenv("CONFIG_LOGGING_PATH", DEFAULT_CONFIG_PATH)

    try:
        with path.open("r") as f:
            logging_config = yaml.safe_load(f)
        logging.config.dictConfig(logging_config)
        logger.info("Logging configured successfully")
    except IOError:
        logging.basicConfig(level=logging.DEBUG)
        logger.warning("logging config file not found, use basic config")
