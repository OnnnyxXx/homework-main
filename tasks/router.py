from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from storage import Storage
from depends import get_storage
# from service import TaskManager, Task
from repository import TaskRepository

from schemas import STaskAdd, STask

router = APIRouter(prefix='/tasks')


@router.get("")
async def get_tasks() -> list[STask]:
   tasks = await TaskRepository.get_tasks()
   return tasks


@router.post("")
async def add_task(task: STaskAdd = Depends()):
   new_task_id = await TaskRepository.add_task(task)
   return {"id": new_task_id}
