from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from pydantic.types import UUID4, Json

from app.core.schema import SchemaBasics, SchemaEmployement, SchemaGroup, SchemaID


class SchemaReward(SchemaBasics):

    title: Optional[str]
    description: Optional[str]
    points: int
    is_expiry_date: Optional[bool]
    valid_from: Any
    valid_till: Any

    employement: SchemaEmployement = None

    class Config:
        orm_mode = True


class CreateRewardSchema(SchemaID):

    title: str
    description: str
    points: int
    is_expiry_date: bool
    valid_from: Any
    valid_till: Any
    employement_id: str

    class Config:
        schema_extra = {
            "example": {
                "title": "sample_reward",
                "description": "sample reward description",
                "points": 10,
                "is_expiry_date": False,
                "valid_from": "01-01-2019",
                "valid_till": "01-01-2019",
                "employement_id": "e4ed8bd6-4caf-40a0-b62b-29b12394ad89",
            }
        }


class UpdateRewardSchema(SchemaID):

    title: str
    description: str
    points: int
    # is_expiry_date: str
    valid_from: Any
    valid_till: Any

    # employement_id: str

    class Config:
        schema_extra = {
            "example": {
                "title": "sample_reward",
                "description": "sample reward description",
                "points": 10,
                # "is_expiry_date": "False",
                "valid_from": "01-01-2019",
                "valid_till": "01-01-2019"
                # "employement_id": "2aad1c2c-b815-4621-9026-b61fc7068a71"
            }
        }
