from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.post_test import PostTest
from ..db import get_db
from ..schemas import robot as robot_schema
from ..cruds import robot as robot_crud
from ..models import robot as robot_model

router = APIRouter()

@router.post("/api/post-test")
async def post_test(
        post_test: PostTest):
    print(post_test)
    pass


@router.post("/api/robots", response_model=robot_schema.RobotCreateResponse)
async def add_robot(
    robot: robot_schema.RobotCreate,
    db: AsyncSession = Depends(get_db)
    ):
    x: robot_model.Robot  = await robot_crud.create_robot(db, robot)
    return x


@router.get("/api/robots", response_model=List[robot_schema.Robot])
async def robot_list(db: AsyncSession = Depends(get_db)):
    robots = await robot_crud.get_robots(db)
    return robots


@router.get("/api/robots/{robot_id:int}", response_model=Optional[robot_schema.Robot])
async def get_robot(robot_id: int, db: AsyncSession = Depends(get_db)):
    robot = await robot_crud.get_robot(db, robot_id)
    return robot


@router.put("/api/robots/{robot_id:int}", response_model=robot_schema.Robot)
async def update_robot(
        robot_id: int,
        robot_create: robot_schema.RobotCreate,
        db: AsyncSession = Depends(get_db)):
    robot = await robot_crud.get_robot(db, robot_id)
    if robot is None:
        raise HTTPException(status_code=404, detail="robot not found")

    robot = await robot_crud.update_robot(db, robot, robot_create)
    return robot


@router.delete("/api/robots/{robot_id:int}")
async def delete_robot(
        robot_id: int,
        db: AsyncSession = Depends(get_db)):
    robot = await robot_crud.get_robot(db, robot_id)
    if robot is None:
        raise HTTPException(status_code=404, detail="robot not found")

    return await robot_crud.delete_robot(db, robot)
