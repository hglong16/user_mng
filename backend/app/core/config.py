from functools import lru_cache
from typing import Any

from pydantic_settings import BaseSettings


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    pass


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
