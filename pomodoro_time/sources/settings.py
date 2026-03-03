"""настройки"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sql_db_name: str | None = 'pomodoro'
