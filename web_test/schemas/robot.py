from pydantic import BaseModel


class Robot(BaseModel):
    id: int
    name: str
    buttery: float
    position: int
    version: str

