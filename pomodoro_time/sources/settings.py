"""настройки"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # sql_db_name: str | None = 'pomodoro'
    # redis_url: str | None = None

    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'password'
    DB_NAME: str = 'pomodoro'
    DB_DRIVER: str = 'postgresql+psycopg'

    CACHE_HOST: str = 'localhost'
    CACHE_PORT: int = 6379
    CACHE_DB: int = 0

    @property
    def database_url(self):
        """база данных"""
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def redis_url(self):
        """кэш"""
        return f'redis://default@{self.CACHE_HOST}:{self.CACHE_PORT}/{self.CACHE_DB}'
