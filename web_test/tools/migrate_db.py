from sqlalchemy.orm import DeclarativeMeta

from web_test.db import engine, Base
from web_test.models import robot


def reset_database():
    if isinstance(Base, DeclarativeMeta):
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
    else:
        raise Exception


if __name__ == "__main__":
    reset_database()
