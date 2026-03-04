"""зависимости"""

from fastapi import Depends
from repository import TaskRepository, TaskCache
from database import session_maker
from cache import redis_session_maker
from service import TaskService


def get_tasks_repository() -> TaskRepository:
    """получить объект репозитория задач"""
    return TaskRepository(session_maker)


def get_tasks_cache() -> TaskCache:
    """получить объект кэша репозитория задач"""
    return TaskCache(redis_session_maker)

def get_tasks_service(tasks_repository: TaskRepository = Depends(get_tasks_repository),
    tasks_cache: TaskCache = Depends(get_tasks_cache)) -> TaskService:
    """получить объект сервис"""

    return TaskService(tasks_repository=tasks_repository, tasks_cache=tasks_cache)

if __name__ == "__main__":
    task_repo = get_tasks_repository()

    tasks = task_repo.get_task_by_category_name('work')
    print(tasks)
    for t in tasks:
        print(t, t.id, t.name, t.pomodoro_count, t.category_id)

    # _task = Task(id=5, name='имя', pomodoro_count=1, category_id=1)
    # task_repo.create_task(_task)

    # task_repo.delete_task(5)
