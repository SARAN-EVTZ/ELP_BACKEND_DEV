from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel
from pydantic.types import UUID4, Json


class SchemaStudent(BaseModel):
    id: int
    enroll: str
    personal_info: Dict
    name: str
    created_on: datetime

    class Config:
        orm_mode = True
