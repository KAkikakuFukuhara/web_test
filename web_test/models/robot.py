from sqlalchemy import Column, Integer, String, ForeignKey, Float

from ..db import Base


class Robot(Base):
    __tablename__ = "robots"

    id = Column(Integer, primary_key=True)
    name = Column(String(1024))
    buttery = Column(Float)
    position = Column(Integer)
    version = Column(String(1024))
