"""формат задач"""

from pydantic import BaseModel, ConfigDict, Field, model_validator


class TaskSchema(BaseModel):
    id: int | None = None
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int = Field(default=None, exclude=True)

    # настройка, чтобы функция model_validate принимала объекты моделей
    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode='after')
    def check_required_fields(self):
        """Проверка: хотя бы одно из полей id или name должно быть задано"""
        if self.id is None and self.name is None:
            raise ValueError('Должен быть указан хотя бы один параметр: id или name')
        return self
