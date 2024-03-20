from decouple import config
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_VERSION: str = config("APP_VERSION", default="1")
    APP_DESCRIPTION: str = config("APP_DESCRIPTION", default="API")
    APP_NAME: str = config("APP_NAME", default="API")
    APP_PORT: int = config("APP_PORT", default=8080, cast=int)
    DB_URL: str = config("DB_URL")
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM_TOKEN: str = config("ALGORITHM_TOKEN", default="HS256")
    EXPIRES_TOKEN: int = config("EXPIRES_TOKEN", default=1140, cast=int)
    ORIGINS: list = [
        "http://localhost:3000",
        "https://localhost:3000",
        "*"
    ]


@lru_cache
def getSettings():
    return Settings()