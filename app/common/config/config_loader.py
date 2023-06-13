import os
from pathlib import Path
from typing import TypeVar

import yaml
from adaptix import Retort

T = TypeVar('T')
DEFAULT_CONFIG_PATH = Path(__file__).parent.parent.parent.parent / "config/config.yml"


def read_yaml(path: str | Path) -> dict:
    with open(path, 'rb') as f:
        return yaml.safe_load(f)


def load_config(config_type: type[T], config_scope: str | None = None, path: str | Path | None = None) -> T:
    if path is None:
        path = os.getenv("CONFIG_PATH", DEFAULT_CONFIG_PATH)

    data = read_yaml(path)

    if config_scope is not None:
        data = data[config_scope]

    dcf = Retort()
    config = dcf.load(data, config_type)
    return config
