
from redis import Redis
from schema.task import TaskSchema
from redis.commands.json.path import Path


class CacheTaskRepository:
    """Репозиторий задач в кэше Redis"""

    def __init__(self, r: Redis):
        self.r = r

    def get_tasks(self) -> list[TaskSchema]:
        """Получить список задач из кэша"""
        list_task_dict = self.r.json().get("tasks:list")
        if list_task_dict is None:
            return []
        list_task_schema = [TaskSchema.model_validate(task_dict) for task_dict in list_task_dict]
        return list_task_schema

    def set_tasks(self, list_task_schema: list[TaskSchema]):
        """Сохранить список задач в кэш"""
        # Преобразуем схемы в словари
        list_task_dict = [task_schema.model_dump() for task_schema in list_task_schema]
        # Сохраняем структуру напрямую
        self.r.json().set("tasks:list", Path.root_path(), list_task_dict)

    def add_task(self, task_schema: TaskSchema):
        """Добавить задачу в конец списка"""
        # Получаем текущий список
        current = self.r.json().get("tasks:list") or []
        # Добавляем новую задачу как словарь
        current.append(task_schema.model_dump())
        # Сохраняем обновлённый список
        self.r.json().set("tasks:list", Path.root_path(), current)

    def clear_tasks(self):
        """Очистить кэш задач"""
        self.r.delete("tasks:list")
