from typing import List

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
async def get_tasks() -> list[STask]:
    """
    Get all tasks from the database
    """
    tasks = await TaskRepository.get_tasks()
    return tasks


@router.post("")
async def add_task(task: STaskAdd = Depends()):
    """
    Saving tasks
    :return tasks.id
    """

    new_task_id = await TaskRepository.add_task(task)
    return {"name": new_task_id}
