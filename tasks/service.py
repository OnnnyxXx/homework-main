from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, PositiveInt, constr

from storage import Storage


class Task(BaseModel):
    id: PositiveInt
    title: constr(min_length=1, max_length=100)
    completed: bool
    created_at: datetime
    updated_at: datetime


class TaskManager:
    def __init__(self, storage: Storage):
        self.storage = storage

    async def get_tasks(self, storage: Storage):
        tasks = await storage.read()
        return tasks

    async def create_task(self, task_data: dict) -> str:
        return await self.storage.create(task_data)
