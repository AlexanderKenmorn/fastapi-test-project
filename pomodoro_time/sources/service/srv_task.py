"""srv_task.py"""

from repository import TaskRepository, TaskCache
from schema.task import TaskSchema
from dataclasses import dataclass


@dataclass
class TaskService:
    """сервисные задачи"""
    tasks_repository: TaskRepository
    tasks_cache: TaskCache

    # (tasks_repository: Annotated[TaskRepository, Depends(get_tasks_repository)],
    # cache_tasks_repository: Annotated[CacheTaskRepository, Depends(get_cache_tasks_repository)]
    # ):

    # def __init__(self, tasks_repository: TaskRepository, tasks_cache: TaskCache):
    #     self.tasks_repository = tasks_repository
    #     self.tasks_cache = tasks_cache

    def get_tasks(self) -> list[TaskSchema]:
        """получить задачи"""
        if list_task_model := self.tasks_cache.get_tasks():
            return list_task_model

        list_task_model = self.tasks_repository.get_tasks()
        list_task_schema = [TaskSchema.model_validate(task_model) for task_model in list_task_model]
        self.tasks_cache.set_tasks(list_task_schema)
        return list_task_model
