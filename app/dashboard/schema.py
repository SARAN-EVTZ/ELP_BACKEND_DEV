
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from pydantic.types import UUID4, Json


class SchemaUserRewardCount(BaseModel):

    title:  str = None
    id:  str = None
    count: str = None

class SchemaBanner(BaseModel):
    title : Optional[str]
    image : Optional[str]
    start_date : Any
    end_date : Any

    class Config:
        orm_mode = True


class CreateSchemaBanner(BaseModel):
    title: str= None
    image: str= None
    start_date: str= None
    end_date: str= None

class UpdateSchemaBanner(BaseModel):
    # id:  str = None
    title : str= None
    image: str=None




