from fastapi import HTTPException
from sqlalchemy import select, delete, update
from database import Task, Category

class TaskRepository:
    """репозиторий задач"""

    def __init__(self, db_session):
        """объект репозитория задач"""
        self.db_session = db_session

    def get_task(self, task_id: int) -> Task:
        """получить задачу по идентификатору"""
        with self.db_session() as session:
            # формируем запрос на выборку всех задач
            query = select(Task).where(Task.id == task_id)
            # выполняем запрос и получаем результат
            query_result = session.execute(query)
            # извлекаем все задачи
            _task = query_result.scalar_one_or_none()
            # проверяем, найдена ли задача
            if _task is None:
                raise HTTPException(status_code=404, detail="Task not found")
        return _task

    def get_tasks(self) -> list[Task]:
        """получить все задачи"""
        with self.db_session() as session:
            # формируем запрос на выборку всех задач
            query = select(Task)
            # выполняем запрос и получаем результат
            query_result = session.execute(query)
            # извлекаем все задачи
            _tasks = query_result.scalars().all()
            # проверяем, найдена ли задача
            if not _tasks:
                raise HTTPException(status_code=404, detail="Tasks not found")
        return _tasks

    def create_task(self, task: Task) -> Task:
        """создать задачу"""
        with self.db_session() as session:
            session.add(task)
            session.commit()
            # Перезагружаем состояние объекта из базы данных, обновляя все его атрибуты актуальными значениями
            session.refresh(task)
            # Открепляем объект от сессии
            session.expunge(task)
        return task

    def update_task(self, task: Task) -> Task:
        """обновить задачу"""
        dict_params = task.to_dict()
        dict_params.pop('id')
        with self.db_session() as session:
            query = update(Task).where(Task.id == task.id).values(**dict_params)
            session.execute(query)
            session.commit()
        return self.get_task(task.id)

    def update_task_name(self, task_id, name) -> Task:
        """обновить наименование задачи"""
        with self.db_session() as session:
            query = update(Task).where(Task.id == task_id).values(name=name)
            session.execute(query)
            session.commit()
        return self.get_task(task_id)

    def delete_task(self, task_id: int):
        """удалить задачу"""
        with self.db_session() as session:
            query = delete(Task).where(Task.id == task_id)
            session.execute(query)
            session.commit()

    def get_task_by_category_name(self, category_name: str) -> list[Task]:
        """получить задачу по имени категории"""
        with self.db_session() as session:
            query = select(Task).join(Category, Task.category_id == Category.id).where(Category.name == category_name)
            # query = select(Task.name, Category.name).select_from(Task).join(Category, Task.category_id == Category.id).where(Category.name == category_name)
            # выполняем запрос и получаем результат
            query_result = session.execute(query)
            # извлекаем все задачи
            _tasks = query_result.scalars().all()
            # проверяем, найдена ли задача
            if not _tasks:
                raise HTTPException(status_code=404, detail="Tasks not found")
        return _tasks
