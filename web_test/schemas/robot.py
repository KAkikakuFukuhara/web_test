from pydantic import BaseModel, Field, ConfigDict

class RobotBase(BaseModel):
    name: str = Field(default="DefaultRobot")
    version: str = Field(default="0.0.0")


class RobotCreate(RobotBase):
    pass


class RobotCreateResponse(RobotCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class Robot(RobotBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

