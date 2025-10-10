from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..models import robot as robot_model
from ..schemas import robot as robot_schema


async def get_robots(
        db: AsyncSession,
    ):
    result = await db.scalars(select(robot_model.Robot))
    return result.all()


async def create_robot(
        db: AsyncSession,
        robot: robot_schema.RobotCreate,
    ) -> robot_model.Robot:
    temp_robot = robot_model.Robot(**robot.model_dump())
    db.add(temp_robot)
    await db.commit()
    await db.refresh(temp_robot)
    return temp_robot


async def get_robot(
        db: AsyncSession,
        robot_id: int
    ):
    result = await db.get(robot_model.Robot, robot_id)
    return result


async def update_robot(
        db: AsyncSession,
        robot: robot_model.Robot,
        robot_create: robot_schema.RobotCreate
    ):
    robot.name = robot_create.name
    robot.version = robot_create.version
    db.add(robot)
    await db.commit()
    await db.refresh(robot)
    return robot


async def delete_robot(
        db: AsyncSession,
        robot: robot_model.Robot
    ):
    await db.delete(robot)
    await db.commit()
