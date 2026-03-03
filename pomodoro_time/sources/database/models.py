
from sqlalchemy import inspect
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from typing import Optional

Base = declarative_base()


class Task(Base):
    """Модель задачи"""
    __tablename__ = 'Tasks'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int]

    def to_dict(self) -> dict:
        """Преобразовать объект в словарь"""
        mapper = inspect(self.__class__)
        return {column.key: getattr(self, column.key)
                for column in mapper.attrs}

class Category(Base):
    """Модель категории"""
    __tablename__ = 'Categories'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[Optional[str]]
    name: Mapped[str]

    def to_dict(self) -> dict:
        """Преобразовать объект в словарь"""
        mapper = inspect(self.__class__)
        return {column.key: getattr(self, column.key)
                for column in mapper.attrs}

