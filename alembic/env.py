
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
from pathlib import Path

# Добавляем корень проекта в sys.path
sys.path.append(str(Path(__file__).parents[1]))

# Объект конфигурации Alembic, который предоставляет
# доступ к значениям в используемом ini-файле.
config = context.config

# Интерпретируйте конфигурационный файл для ведения журнала на Python.
# Эта строка в основном настраивает логгеры.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# URL-адрес базы данных из настроек окружающей среды (Загружаем Settings настройки ДО импорта моделей)
# sqlite:/// - относительный путь
from pomodoro_time.sources.settings import Settings
settings = Settings()
database_url = f'postgresql+psycopg://postgres:password@localhost:5432/{settings.sql_db_name}'

# Метаданные ваших моделей
# Для поддержки автогенерации необходимо указать переменную target_metadata с метаданными ваших таблиц.
from pomodoro_time.sources.database.models import Base
target_metadata = Base.metadata

# могут быть получены другие значения из конфигурации, определенные в соответствии с требованиями env.py
# my_important_option = config.get_main_option("my_important_option")

def run_migrations_offline() -> None:
    """Выполняйте миграцию в "автономном" режиме.

    Это настраивает контекст с помощью простого URL-адреса
    и не двигатель, хотя двигатель вполне приемлем
    и здесь тоже.  Пропустив создание движка
    нам даже не нужен DBAPI, чтобы быть доступными.

    Вызовы context.execute() здесь передают заданную строку
    в выходные данные скрипта.

    """
    context.configure(
        url=database_url,  # ← Используем URL-адрес из настроек
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Запустите миграцию в режиме "онлайн".

    В этом случае нам нужно создать движок
    и связать соединение с контекстом.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        url=database_url,  # ← Используем URL-адрес из настроек
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
