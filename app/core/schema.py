from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from pydantic.types import UUID4, Json


class SchemaID(BaseModel):
    id: Optional[UUID4] = Field(default=None, primary_key=True)


class SchemaBasics(SchemaID):

    created_at: datetime
    updated_at: datetime
    is_deleted: bool
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class SchemaGroup(SchemaBasics):

    name: str
    description: str = None

    class Config:
        orm_mode = True


class SchemaEmployement(SchemaBasics):

    name: str
    description: str = None

    class Config:
        orm_mode = True


class SchemaMode(SchemaBasics):

    name: str
    description: str = None

    class Config:
        orm_mode = True
