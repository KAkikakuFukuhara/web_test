from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..models import task as task_model
from ..schemas import task as task_schema
from ..models import robot as robot_model


async def get_tasks(
        db: AsyncSession
    ) -> Sequence[task_model.Task]:
    result = await db.scalars(select(task_model.Task))
    return result.all()


async def add_task(
        db: AsyncSession,
        robot: robot_model.Robot,
        task_create: task_schema.TaskCreate
    ) -> task_model.Task:
    task = task_model.Task(**task_create.model_dump())
    robot.tasks.append(task)
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_task(
        db: AsyncSession,
        task_id: int
    ) -> Optional[task_model.Task]:
    task = await db.scalar(select(task_model.Task).where(task_model.Task.id == task_id))
    return task


async def delete_task(
        db: AsyncSession,
        task: task_model.Task
    ):
    await db.delete(task)
    await db.commit()


async def update_done(
        db: AsyncSession,
        task: task_model.Task,
        task_update: task_schema.TaskUpdate
    ) -> task_model.Task:
    task.done = task_update.done
    await db.commit()
    await db.refresh(task)
    return task
