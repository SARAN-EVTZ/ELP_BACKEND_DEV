from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from pydantic.types import UUID4, Json

from app.core.schema import SchemaBasics, SchemaEmployement, SchemaGroup, SchemaID
from app.reward.schema import SchemaReward


class SchemaUser(SchemaBasics):

    employee_id: Optional[str]
    email_id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    dob: Any
    gender: Optional[str]
    designation: Optional[str]
    employement: SchemaEmployement = None
    group: SchemaGroup = None

    class Config:
        orm_mode = True


class SchemaUserReward(SchemaBasics):

    user_id:  SchemaID = None
    reward_id:  SchemaID = None
    citation_id: SchemaID = None
    comment: Optional[str]
    certificate: Optional[str]
    is_uploaded: Optional[bool]
    citation: SchemaUser = None
    reward: SchemaReward = None
    user: SchemaUser = None

    class Config:
        orm_mode = True


class CreateUserSchema(BaseModel):

    employee_id: str
    email_id: str
    first_name: str
    last_name: str
    phone_number: str
    dob: Any
    gender: str
    designation: str
    group_id: str
    employement_id: str

    class Config:
        schema_extra = {
            "example": {
                "employee_id": "EITS0001",
                "email_id": "User1@evolutyz.com",
                "first_name": "User1",
                "last_name": "evolutyz",
                "phone_number": "xxxxxxxxxx",
                "dob": "01-01-2019",
                "gender": "M",
                "designation": "Developer",
                "group_id": "1a82e1f7-c7de-4e7c-8093-d50af109ca62",
                "employement_id": "e4ed8bd6-4caf-40a0-b62b-29b12394ad89",
            }
        }


class SchemaAssignReward(BaseModel):

    user_id:  str
    reward_id:  str
    citation_id: str
    comment:  str
    certificate: str
    is_uploaded: bool

    class Config:
        schema_extra = {
            "example": {
                "user_id": "59ec4f08-550c-419d-9037-1a248f52654e",
                "reward_id": "9567c452-7962-4236-b044-78548b9c2e37",
                "comment": "ADD YOUR COMMENT HERE",
                "citation_id": "e0b5c47f-4c32-4b50-933b-c11fcbeda77a",
                "certificate": "",
                "is_uploaded": False
            }
        }
