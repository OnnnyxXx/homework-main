from sqlalchemy import select
from database import TaskOrm, new_session
from schemas import STaskAdd, STask

from database import TaskOrm, new_session


async def add_task(data: dict) -> int:
    async with new_session() as session:
        new_task = TaskOrm(**data)
        session.add(new_task)
        await session.flush()
        await session.commit()
        return new_task.id


async def get_tasks():
    async with new_session() as session:
        query = select(TaskOrm)
        result = await session.execute(query)
        task_models = result.scalars().all()
        return task_models


class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            data = task.model_dump()
            new_task = TaskOrm(**data)
            session.add(new_task)
            await session.flush()
            await session.commit()
            return new_task.id

    @classmethod
    async def get_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [STask.model_validate(task_model) for task_model in task_models]
            return tasks
