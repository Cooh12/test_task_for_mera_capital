import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class DBConfig:
    type: str | None = None
    connector: str | None = None
    host: str | None = None
    port: int | None = None
    login: str | None = None
    password: str | None = None
    name: str | None = None
    path: str | None = None
    echo: bool = False

    @property
    def uri(self) -> str:
        if self.type in ('mysql', 'postgresql'):
            url = (
                f'{self.type}+{self.connector}://'
                f'{self.login}:{self.password}'
                f'@{self.host}:{self.port}/{self.name}'
            )
        elif self.type == 'sqlite':
            url = f'{self.type}://{self.path}'
        else:
            raise ValueError('DB_TYPE not MySQL, SQLite or Postgres')
        logger.debug(url)
        return url
