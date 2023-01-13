from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page, add_pagination, paginate
from loguru import logger
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse


from fastapi_filter import FilterDepends


from app.db.session import get_db
from app.user import crud as user_crud
from app.user.models import User
from app.user.schema import CreateUserSchema, SchemaUser, SchemaAssignReward

from app.user.filter import UserFilter

router = APIRouter()


# _query = select([
#     Reward.title,
#     UserReward.reward_id,
#     func.count(UserReward.reward_id).label("count")
# ]).group_by(UserReward.reward_id, Reward.title)

# result = db.execute(statement)

# for i in result:
#     print("\n", i)


# @router.get("/FromAd")
# async def get_users_from_ad():
#     pass


# @router.get("/syncAdtoDB")
# async def sync_ad_with_db():
#     pass


@router.get(
    "/all", status_code=status.HTTP_200_OK, response_model=Page[SchemaUser]
)
async def get_users_from_db(db: Session = Depends(get_db)):

    data = user_crud.get_users_from_db(db)

    return paginate(data)


@router.post("/create")
async def create_user(user: CreateUserSchema, db: Session = Depends(get_db)):

    data = user_crud.get_user(
        db=db, email_id=user.email_id, employee_id=user.employee_id
    )

    if data is not None:
        return JSONResponse(
            status_code=400, content={"message": "user already exist"}
        )

    data = user_crud.create_user(db=db, user=user)
    if data is None:
        return JSONResponse(
            status_code=500, content={"message": "Internal Server Error"}
        )

    return JSONResponse(status_code=200, content={"message": "success"})


@router.put("/update")
async def update_user():

    data = user_crud.update_user(user_id=user_id, user=user, db=db)

    if data is None:
        return JSONResponse(
            status_code=500, content={"message": "Internal Server Error"}
        )
    return data


@router.get(
    "/me/{id}", status_code=status.HTTP_200_OK, response_model=SchemaUser
)
async def me(id: str, db: Session = Depends(get_db)):
    try:
        return user_crud.get_me_from_db(db, id)
    except Exception as e:
        logger.error(e)


@router.delete("/{id}")
async def delete_user(id: str):
    """Delete A User"""
    data = user_crud.delete_user(id=id, db=db)

    if data is None:
        return JSONResponse(
            status_code=500, content={"message": "Internal Server Error"}
        )
    return JSONResponse(status_code=200, content={"message": "success"})


@router.post("/assignreward")
async def assign_reward(details: SchemaAssignReward, db: Session = Depends(get_db)):

    data = user_crud.create_user_reward(db=db, details=details)

    if data is None:
        return JSONResponse(
            status_code=500, content={"message": "Internal Server Error"}
        )

    return JSONResponse(status_code=200, content={"message": "success"})
