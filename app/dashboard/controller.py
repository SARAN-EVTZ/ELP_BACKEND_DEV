from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page, add_pagination, paginate
from loguru import logger
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse


from app.dashboard import crud as dashboard_crud
from app.dashboard.schema import SchemaUserRewardCount, CreateSchemaBanner, SchemaBanner , UpdateSchemaBanner

from app.db.session import get_db


router = APIRouter()


@router.get(
    "/assignedRewardCount", status_code=status.HTTP_200_OK, response_model=Page[SchemaUserRewardCount]
)
async def assigned_reward_count(db: Session = Depends(get_db)):

    data = dashboard_crud.get_assigned_reward_count(db)

    logger.info(type(data))

    return paginate(data)


@router.post(
    "/banner/create", status_code=status.HTTP_201_CREATED,
)
async def add_banner(banner: CreateSchemaBanner, db: Session = Depends(get_db)):
    data = dashboard_crud.create_banner(db=db, banner=banner)
    if data is None:
        return JSONResponse(
            status_code=404, content={"Message": "Banner Already Exists"}
            )
    return JSONResponse(
        status_code=200, content={"Message": "Banner Created Successfully"}
        )


@router.get(
    "/banner/all", status_code=status.HTTP_200_OK, response_model=Page[SchemaBanner]
)
async def get_banner( db: Session = Depends(get_db)):
    data = dashboard_crud.get_banner_from_db(db)

    logger.info(data)

    return paginate(data)



@router.delete("/banner/{title}", status_code=status.HTTP_200_OK)
async def delete_banner(title: str , db:Session = Depends(get_db)):
    """Delete A Banner"""
    data = dashboard_crud.delete_banner(title=title, db=db)

    if data is None:
        return JSONResponse(
            status_code=500, content={"message": "Internal Server Error"}
        )
    return JSONResponse(status_code=200, content={"message": "success"})



@router.put("/banner/{id}", status_code=status.HTTP_200_OK,)

async def update_banner( id: str , banner: UpdateSchemaBanner, db: Session = Depends(get_db)):
    """Update A Banner"""
    data = dashboard_crud.update_banner(banner=banner , db = db)

    if data is None:
        return JSONResponse(
            status_code=500 , content={"message" : "Internal Server Error"}
        )
    return JSONResponse(status_code=200 , content={"message" : "Banner Updated Successfully"})
