from typing import TYPE_CHECKING, List

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship

from ..db import Base

if TYPE_CHECKING:
    from .task import Task


class Robot(Base):
    __tablename__ = "robots"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(1024))
    version: Mapped[str] = mapped_column(String(1024))

    tasks: Mapped[List["Task"]] = relationship(
        back_populates="robot",
        lazy="selectin",
        cascade="all, delete-orphan")

