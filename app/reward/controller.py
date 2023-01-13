from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page, add_pagination, paginate
from starlette.responses import JSONResponse


from loguru import logger
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.reward import crud as reward_crud
from app.reward.schema import CreateRewardSchema, SchemaReward, UpdateRewardSchema

router = APIRouter()


@router.get(
    "/all", status_code=status.HTTP_200_OK, response_model=Page[SchemaReward]
)
async def get_all_rewards(db: Session = Depends(get_db)):
    """Return All Rewards"""

    data = reward_crud.get_all_rewards(db)

    return paginate(data)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=SchemaReward)
async def get_one_reward():
    return reward_crud.get_one_reward(db)


@router.post("/create")
async def create_reward(
    reward: CreateRewardSchema, db: Session = Depends(get_db)
):

    data = reward_crud.create_reward(db=db, reward=reward)
    if data is None:
        return JSONResponse(
            status_code=404, content={"message": "Reward already exists"}
        )

    return JSONResponse(status_code=200, content={"message": "success"})


@router.put("/update")
async def update_reward(id: str, reward: UpdateRewardSchema, db: Session = Depends(get_db)):

    data = reward_crud.update_reward(reward_id=id, reward=reward, db=db)

    if data is None:
        return JSONResponse(
            status_code=500, content={"message": "Internal Server Error"}
        )
    return data


@router.delete("/{id}")
async def delete_reward(id: str,  db: Session = Depends(get_db)):
    """Delete A reward"""
    data = reward_crud.delete_reward(id=id, db=db)

    if data is None:
        return JSONResponse(
            status_code=500, content={"message": "Internal Server Error"}
        )

    return JSONResponse(status_code=200, content={"message": "success"})
