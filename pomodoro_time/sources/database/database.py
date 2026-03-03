"""работа с базой данных"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pomodoro_time.sources.settings import Settings

settings = Settings()

engine = create_engine(f'postgresql+psycopg://postgres:password@localhost:5432/{settings.sql_db_name}',
                       connect_args={
                           "connect_timeout": 10,  # Таймаут подключения (сек)
                           "options": "-c statement_timeout=30000"  # Таймаут запроса (мс)
                       })

session_maker = sessionmaker(autocommit=False, autoflush=True, bind=engine)
