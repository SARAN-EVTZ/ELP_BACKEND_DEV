from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger
from sqlalchemy.orm import Session

from app.auth.auth_bearer import JWTBearer
from app.db.session import get_db
from app.sample import crud as sample_crud
from app.sample.models import Student
from app.sample.schema import SchemaStudent

router = APIRouter()


@router.get(
    "/all", status_code=status.HTTP_200_OK, response_model=List[SchemaStudent]
)
async def get_all_sample_data(db: Session = Depends(get_db)):

    try:
        return sample_crud.get_user_from_ad(db)
    except Exception as e:
        logger.error(e)


@router.get("/one")
async def get_one_sample_data():
    pass


@router.post("/create", dependencies=[Depends(JWTBearer())])
async def create_sample():
    pass


@router.put("/update")
async def update_sample():
    pass


@router.delete("/delete")
async def delete_sample():
    pass
