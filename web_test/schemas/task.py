from typing import List

from pydantic import BaseModel


class Task(BaseModel):
    task_list: List[int]
    dones: List[int]
