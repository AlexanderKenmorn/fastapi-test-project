"""настройки"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sql_db_name: str | None = 'pomodoro'
    redis_url: str | None = None
