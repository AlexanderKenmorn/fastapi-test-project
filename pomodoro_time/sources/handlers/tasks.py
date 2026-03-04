"""задачи"""

from fastapi import APIRouter, status, HTTPException, Depends
from typing import Annotated
from dependecy import get_tasks_repository, get_tasks_cache, get_tasks_service
from repository import TaskRepository, TaskCache
from schema.task import TaskSchema
from database import Task
from service.srv_task import TaskService

# tasks = [TaskSchema(**_t) for _t in fixtures_tasks]

router = APIRouter(prefix='/task', tags=['task'])


@router.get(
    '/all',
    response_model=list[TaskSchema]
)
async def get_tasks(tasks_service: Annotated[TaskService, Depends(get_tasks_service)]) -> list[TaskSchema]:
    """task/all"""
    return tasks_service.get_tasks()
    # connection = get_db_connection()
    # cursor = connection.cursor()
    # fixtures_tasks = cursor.execute("SELECT * FROM Tasks").fetchall()
    # tasks = [TaskSchema(
    #     id=fixed_task[0],
    #     name=fixed_task[1],
    #     pomodoro_count=fixed_task[2],
    #     category_id=fixed_task[3]
    # ) for fixed_task in fixtures_tasks]
    # connection.close()
    # return tasks
    # if list_task_model := cache_tasks_repository.get_tasks():
    #     return list_task_model
    #
    # list_task_model = tasks_repository.get_tasks()
    # list_task_schema = [TaskSchema.model_validate(task_model) for task_model in list_task_model]
    # cache_tasks_repository.set_tasks(list_task_schema)
    # return list_task_model


@router.post(
    '/',
    response_model=TaskSchema
)
async def create_task(task_schema: TaskSchema,
                      tasks_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
                      ):
    """task/"""
    # # Ищем задачу (один элемент)
    # _task = next((_t for _t in tasks if _t.id == task_schema.id), None)
    # # Если задача не найдена — добавляем её
    # if not _task:
    #     tasks.append(task_schema)
    # # Если задача существует, то вызываем ошибку клиента
    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail=f"задача не может быть создана, id:{task_schema.id} уже существует"
    #     )
    # print(f'--> создана задача "{task_schema.name}"')
    # return task_schema
    # connection = get_db_connection()
    # cursor = connection.cursor()
    # cursor.execute(
    #     "INSERT INTO Tasks (name, pomodoro_count, category_id) VALUES (?,?,?)",
    #     (task_schema.name, task_schema.pomodoro_count, task_schema.category_id)
    # )
    # connection.commit()
    # connection.close()
    # return task_schema
    task_model = Task(name=task_schema.name,
                      pomodoro_count=task_schema.pomodoro_count,
                      category_id=task_schema.category_id)
    task_model = tasks_repository.create_task(task_model)
    return task_model


@router.put(
    '/{task_id}',
    response_model=TaskSchema,
    status_code=status.HTTP_200_OK,
    summary='Обновить задачу',
    description='Обновляет задачу по идентификатору'
)
# async def update_task(task_id: int, name: str, pomodoro_count: int, category_id: int):
async def update_task(task_id: int,
                      task_schema: TaskSchema,
                      tasks_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
                      ):
    """task/{task_id}
    обновляет задачу
    """
    if (task_schema.id is not None) and (task_schema.id != task_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"id:{task_id} задачи не может быть изменён"
        )
    # # Ищем задачу (один элемент)
    # _task = next((_t for _t in tasks if _t.id == task_id), None)
    # # Если задача не найдена — ошибка 404
    # if not _task:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"Задача id:{task_id} не найдена"
    #     )
    # elif task_schema.id != task_id:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail=f"id:{task_id} задачи не может быть изменён"
    #     )
    # # Обновляем поля
    # else:
    #     _task.name = task_schema.name
    #     _task.pomodoro_count = task_schema.pomodoro_count
    #     _task.category_id = task_schema.category_id
    # print(f'--> задача id:{task_id} обновлена')
    # return task_schema
    #
    # connection = get_db_connection()
    # cursor = connection.cursor()
    # cursor.execute(
    #     "UPDATE Tasks SET name =?, pomodoro_count =?, category_id =? WHERE id =?",
    #     (task_schema.name, task_schema.pomodoro_count, task_schema.category_id, task_id)
    # )
    # connection.commit()
    # connection.close()
    # return task_schema
    task_model = Task(id=task_id,
                      name=task_schema.name,
                      pomodoro_count=task_schema.pomodoro_count,
                      category_id=task_schema.category_id)
    task_model = tasks_repository.update_task(task_model)
    return task_model


@router.patch(
    '/{task_id}',
    response_model=TaskSchema,
    status_code=status.HTTP_200_OK
)
async def patch_task(task_id: int, name: str,
                     tasks_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
                     ):
    """task/{task_id}
    обновляет имя задачи
    """
    # # Ищем задачу (один элемент)
    # task_schema = next((_t for _t in tasks if _t.id == task_id), None)
    # # Если задача не найдена — ошибка 404
    # if not task_schema:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"Задача id:{task_id} не найдена"
    #     )
    # # Обновляем имя
    # else:
    #     task_schema.name = name
    # print(f'--> имя задачи {task_id} было заменено на {name}')
    # return task_schema
    #
    # connection = get_db_connection()
    # cursor = connection.cursor()
    # cursor.execute(
    #     "UPDATE Tasks SET name =? WHERE id =?",
    #     (name, task_id)
    # )
    # connection.commit()
    # fixed_task = cursor.execute("SELECT * FROM Tasks WHERE id =?", (task_id ,)).fetchall()[0]
    # connection.close()
    # return TaskSchema(
    #     id=fixed_task[0],
    #     name=fixed_task[1],
    #     pomodoro_count=fixed_task[2],
    #     category_id=fixed_task[3]
    # )
    task_model = tasks_repository.update_task_name(task_id, name)
    return task_model


@router.delete(
    '/{task_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_task(task_id: int,
                      tasks_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
                      ):
    """task/{task_id}
    удаляет задачу
    """
    # # Ищем задачу (один элемент)
    # task_schema = next((_t for _t in tasks if _t.id == task_id), None)
    # # Если задача не найдена — ошибка 404
    # if not task_schema:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"Задача id:{task_id} не найдена"
    #     )
    # # Удаляем задачу
    # else:
    #     tasks.remove(task_schema)
    # print(f'--> задача {task_id} удалена')
    # return f'--> задача {task_id} удалена'
    #
    # connection = get_db_connection()
    # cursor = connection.cursor()
    # fixed_task = cursor.execute("SELECT * FROM Tasks WHERE id =?", (task_id,)).fetchall()[0]
    # cursor.execute("DELETE FROM Tasks WHERE id =?", (task_id,))
    # connection.commit()
    # connection.close()
    # return TaskSchema(
    #     id=fixed_task[0],
    #     name=fixed_task[1],
    #     pomodoro_count=fixed_task[2],
    #     category_id=fixed_task[3]
    # )
    tasks_repository.delete_task(task_id)
    return None

