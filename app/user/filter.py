from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Any, Dict, List, Optional


from app.user.models import User


class UserFilter(Filter):
    employee_id: Optional[str]
    first_name: Optional[str]

    class Constants(Filter.Constants):
        model = User
