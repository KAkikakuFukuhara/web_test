from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    done: bool = False


class TaskCreate(TaskBase):
    lane_number: int
    robot_id: int = Field(ge=1)


class TaskUpdate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    robot_id: int
    lane_number: int

