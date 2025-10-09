from pydantic import BaseModel, model_validator
import json

class PostTest(BaseModel):
    radio: str
    text: str