from sqlalchemy import select
from schemas import STaskAdd, STask
from database import TaskOrm, new_session


class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            data = task.model_dump()
            new_task = TaskOrm(**data)
            session.add(new_task)
            await session.flush()
            await session.commit()
            return new_task.name  # if not need task.id

    @classmethod
    async def get_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [STask.model_validate(task_model) for task_model in task_models]
            return tasks

    @classmethod
    async def delete_task(cls, task_id: int) -> str:
        async with new_session() as session:
            task = await session.get(TaskOrm, task_id)
            if task:
                await session.delete(task)
                await session.commit()
                return f"delete={task.name} id={task.id}"
            else:
                return f"Task with id={task_id} not found"
