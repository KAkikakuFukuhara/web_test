from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite:///fastapi_app.db"

engine: Engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessiongLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    with SessiongLocal() as session:
        yield session
