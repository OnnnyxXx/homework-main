from typing import List, Dict

from fastapi import APIRouter, Depends, status, HTTPException

from storage import Storage
from depends import get_storage
# from service import TaskManager, Task
from repository import TaskRepository

from schemas import STaskAdd, STask

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


@router.post("")
async def add_task(task: STaskAdd = Depends()):
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
