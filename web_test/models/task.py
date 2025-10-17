from typing import List, TYPE_CHECKING
from sqlalchemy import Column, Integer, ARRAY, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from ..db import Base

import json

if TYPE_CHECKING:
    from .robot import Robot


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int]  = mapped_column(primary_key=True)
    lane_number: Mapped[int] = mapped_column(Integer)
    done: Mapped[int] = mapped_column(Integer)
    robot_id: Mapped[int] = mapped_column(ForeignKey("robots.id"))

    robot: Mapped["Robot"] = relationship(back_populates="tasks")
