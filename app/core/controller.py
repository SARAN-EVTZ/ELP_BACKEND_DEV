from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page, add_pagination, paginate
from loguru import logger
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.schema import SchemaGroup, SchemaEmployement, SchemaMode
from app.core import crud as core_crud

router = APIRouter()


@router.get(
    "/groups_all", status_code=status.HTTP_200_OK, response_model=Page[SchemaGroup]
)
async def get_all_groups(db: Session = Depends(get_db)):
    """Return All groups"""

    data = core_crud.get_all_groups(db)

    return paginate(data)


@router.get(
    "/employements_all", status_code=status.HTTP_200_OK, response_model=Page[SchemaEmployement]
)
async def get_all_employements(db: Session = Depends(get_db)):
    """Return All employements"""

    data = core_crud.get_all_employements(db)

    return paginate(data)


@router.get(
    "/modes_all", status_code=status.HTTP_200_OK, response_model=Page[SchemaMode]
)
async def get_all_modes(db: Session = Depends(get_db)):
    """Return All modes"""

    data = core_crud.get_all_modes(db)

    return paginate(data)
