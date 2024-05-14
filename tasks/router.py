from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from storage import Storage
from depends import get_storage
from service import TaskManager, Task

router = APIRouter(prefix='/tasks')


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[Task])
async def tasks(storage: Storage = Depends(get_storage)):
    """
    Route to view all tasks

    :param storage: actual storage instance
    """
    tasks_data = await storage.read()

    return tasks_data


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(task: Task):
    """
    Route for create new task in storage and returned her name

    :param task: Task entity
    :return: task name
    """
    return task.title
