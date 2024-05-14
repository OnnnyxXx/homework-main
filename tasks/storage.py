import json
import os
import uuid
from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Storage(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def save(self, task_data: Any):
        pass

    @abstractmethod
    async def create(self, task_data):
        pass


class JSONStorage(Storage):
    def __init__(self, file_path):
        self.file_path = file_path

    async def read(self) -> List[Dict[str, Any]]:
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        return data.get('tasks', [])

    async def save(self, tasks: List[Dict[str, Any]]) -> None:
        with open(self.file_path, 'w') as file:
            json.dump({'tasks': tasks}, file, indent=4)

    async def create(self, task_data: Dict[str, Any]) -> str:
        tasks = await self.read()
        task_id = str(uuid.uuid4())
        task_data['id'] = task_id
        tasks.append(task_data)
        await self.save(tasks)
        return task_id
