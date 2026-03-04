"""cache_task.py"""

import logging
from schema.task import TaskSchema
from redis.exceptions import ResponseError

logger = logging.getLogger(__name__)


def try_decorator(method):
    """обработка ошибок RedisJSON"""

    def wrapper(self, *args, **kwargs):
        """обёртка"""
        try:
            return method(self, *args, **kwargs)
        except ResponseError as e:
            logger.error(f'❌ RedisJSON error: {e}')
            return []  # или raise, в зависимости от стратегии
        except Exception as e:
            logger.exception(f'❌ Unexpected error in get_tasks: {e}')
            raise

    return wrapper


class TaskCache:
    """Репозиторий задач в кэше Redis"""

    def __init__(self, redis_session_maker):
        self.redis_session_maker = redis_session_maker

    @try_decorator
    def get_tasks(self) -> list[TaskSchema]:
        """Получить список задач из кэша"""
        with self.redis_session_maker() as r:
            list_task_dict = r.json().get('tasks:list')
            if list_task_dict is None:
                return []
            list_task_schema = [TaskSchema.model_validate(task_dict) for task_dict in list_task_dict]
            return list_task_schema

    @try_decorator
    def set_tasks(self, list_task_schema: list[TaskSchema], ttl: int = 3600) -> None:
        """Сохранить список задач в кэш"""
        with self.redis_session_maker() as r:
            # Преобразуем схемы в словари
            list_task_dict = [task_schema.model_dump() for task_schema in list_task_schema]
            # Сохраняем структуру напрямую
            r.json().set('tasks:list', '$', list_task_dict)
            r.expire('tasks:list', ttl)  # 🔥 Авто-удаление

    @try_decorator
    def add_task(self, task_schema: TaskSchema) -> None:
        """Добавить задачу в конец списка"""
        with self.redis_session_maker() as r:
            # JSON.ARRAPPEND добавляет элемент в массив без чтения всего документа
            r.json().arrappend('tasks:list', '$', task_schema.model_dump())

    @try_decorator
    def clear_tasks(self) -> None:
        """Очистить кэш задач"""
        with self.redis_session_maker() as r:
            r.delete('tasks:list')
