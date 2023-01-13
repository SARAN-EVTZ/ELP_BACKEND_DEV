from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel
from pydantic.types import UUID4, Json


class HealthResponseSchema(BaseModel):
    db: str

    class config:
        schema_extra = {"example": {"status": "OK"}}
