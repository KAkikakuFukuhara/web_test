from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.post_test import PostTest
from ..db import get_db
from ..schemas import robot as robot_schema
from ..cruds import robot as robot_crud
from ..models import robot as robot_model
from ..schemas import task as task_schema
from ..cruds import task as task_crud
from ..models import task as task_model


TAG_ROBOTS = "api/robots"
TAG_TASKS = "api/tasks"


router = APIRouter()


@router.get("/api/hello")
async def hello():
    return {"message": "hello worlds!"}


@router.post("/api/post-test")
async def post_test(
        post_test: PostTest):
    print(post_test)
    pass


@router.post(
    "/api/robots",
    response_model=robot_schema.RobotCreateResponse,
    tags=[TAG_ROBOTS])
async def add_robot(
    robot: robot_schema.RobotCreate,
    db: AsyncSession = Depends(get_db)
    ):
    x: robot_model.Robot  = await robot_crud.create_robot(db, robot)
    return x


@router.get(
    "/api/robots",
    response_model=List[robot_schema.Robot],
    tags=[TAG_ROBOTS])
async def robot_list(db: AsyncSession = Depends(get_db)):
    robots = await robot_crud.get_robots(db)
    return robots


@router.get(
    "/api/robots/{robot_id:int}",
    response_model=Optional[robot_schema.Robot],
    tags=[TAG_ROBOTS])
async def get_robot(robot_id: int, db: AsyncSession = Depends(get_db)):
    robot = await robot_crud.get_robot(db, robot_id)
    return robot


@router.put(
    "/api/robots/{robot_id:int}",
    response_model=robot_schema.Robot,
    tags=[TAG_ROBOTS])
async def update_robot(
        robot_id: int,
        robot_create: robot_schema.RobotCreate,
        db: AsyncSession = Depends(get_db)):
    robot = await robot_crud.get_robot(db, robot_id)
    if robot is None:
        raise HTTPException(status_code=404, detail="robot not found")

    robot = await robot_crud.update_robot(db, robot, robot_create)
    return robot


@router.delete(
    "/api/robots/{robot_id:int}",
    tags=[TAG_ROBOTS])
async def delete_robot(
        robot_id: int,
        db: AsyncSession = Depends(get_db)):
    robot = await robot_crud.get_robot(db, robot_id)
    if robot is None:
        raise HTTPException(status_code=404, detail="robot not found")

    return await robot_crud.delete_robot(db, robot)


@router.get(
    "/api/robots/{robot_id:int}/tasks",
    response_model=List[task_schema.Task],
    tags=[TAG_ROBOTS, TAG_TASKS])
async def get_robot_tasks(
        robot_id: int,
        db: AsyncSession = Depends(get_db)
    ):
    robot = await robot_crud.get_robot(db, robot_id)
    if robot is None:
        raise HTTPException(status_code=404, detail="robot not found")

    return robot.tasks


@router.get(
    "/api/tasks",
    response_model=List[task_schema.Task],
    tags=[TAG_TASKS])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    tasks = await task_crud.get_tasks(db)
    return tasks


@router.post(
    "/api/tasks",
    response_model=task_schema.Task,
    tags=[TAG_TASKS])
async def add_task(
        task_create: task_schema.TaskCreate,
        db: AsyncSession = Depends(get_db)):
    robot = await robot_crud.get_robot(db, task_create.robot_id)
    if robot is None:
        raise HTTPException(status_code=404, detail="robot not found")

    task: task_model.Task = await task_crud.add_task(db, robot, task_create)
    return task


@router.get(
    "/api/tasks/{task_id:int}",
    response_model=task_schema.Task,
    tags=[TAG_TASKS])
async def get_task(
        task_id: int,
        db: AsyncSession = Depends(get_db)
    ):
    task = await task_crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")

    return task


@router.delete(
    "/api/tasks/{task_id:int}",
    tags=[TAG_TASKS])
async def delete_task(
        task_id: int,
        db: AsyncSession = Depends(get_db)
    ):
    task = await task_crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")

    return await task_crud.delete_task(db, task)


@router.put(
    "/api/tasks/{task_id:int}",
    response_model=task_schema.Task,
    tags=[TAG_TASKS])
async def update_done(
        task_id: int,
        task_update: task_schema.TaskUpdate,
        db: AsyncSession = Depends(get_db)
    ):
    task = await task_crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")

    return await task_crud.update_done(db, task, task_update)
