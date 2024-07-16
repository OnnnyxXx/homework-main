from fastapi import APIRouter, Depends, status, HTTPException
from repository import TaskRepository
from schemas import STaskAdd

router = APIRouter(
    prefix='/tasks',
    tags=['Задачи']
)


@router.get("")
async def get_tasks():
    """
    Get all tasks from the database
    """
    try:
        tasks = await TaskRepository.get_tasks()
        return {
            'status': 'success',
            'data': tasks,
            'details': None
        }

    except Exception:
        raise HTTPException(status_code=400, detail={
            "status": 'not tasks',
            'data': None,
            'details': None,
        })


@router.post("/add/tasks")
async def add_task(task: STaskAdd):
    """
    Saving tasks
    :return tasks.id
    """
    try:
        new_task_id = await TaskRepository.add_task(task)
        return {
            'status': status.HTTP_200_OK,
            "name": new_task_id,
        }
    except Exception:
        raise HTTPException(status_code=400, detail={
            "status": 'error fields',
            'data': None,
            'details': None,
        })


@router.delete("/delete/{tasks_id}")
async def delete_tasks(tasks_id):
    """
    Delete tasks from the database
    """
    try:
        result = await TaskRepository.delete_task(tasks_id)
        return {
            'status': 'success',
            'data': result,
            'details': None
        }

    except Exception:
        raise HTTPException(status_code=400, detail={
            "status": 'not tasks',
            'data': None,
            'details': None,
        })
