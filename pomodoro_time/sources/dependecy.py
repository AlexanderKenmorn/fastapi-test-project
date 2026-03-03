"""зависимости"""

from repository import TaskRepository, CacheTaskRepository
from database import session_maker
from cache import get_redis_connection


def get_tasks_repository() -> TaskRepository:
    """получить объект репозитория задач"""
    return TaskRepository(session_maker)


def get_cache_tasks_repository() -> CacheTaskRepository:
    """получить объект кэша репозитория задач"""
    redis_connection = get_redis_connection()
    return CacheTaskRepository(redis_connection)


if __name__ == "__main__":
    task_repo = get_tasks_repository()

    tasks = task_repo.get_task_by_category_name('work')
    print(tasks)
    for t in tasks:
        print(t, t.id, t.name, t.pomodoro_count, t.category_id)

    # _task = Task(id=5, name='имя', pomodoro_count=1, category_id=1)
    # task_repo.create_task(_task)

    # task_repo.delete_task(5)
