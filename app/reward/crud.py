from datetime import datetime, timezone
from typing import Any

from fastapi import HTTPException
from loguru import logger

from sqlalchemy import exc
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


from app.reward.models import Reward
from app.reward.schema import CreateRewardSchema, UpdateRewardSchema


def get_all_rewards(db: Session):
    try:

        return db.query(Reward).filter(Reward.is_deleted == False).all()

    except SQLAlchemyError as e:
        return None


def get_one_reward(db: Session):
    try:

        return db.query(Reward).filter(Reward.is_deleted == False).first()

    except SQLAlchemyError as e:
        return None


def create_reward(db: Session, reward: CreateRewardSchema) -> Any:
    """Add New Reward"""

    try:

        db_reward = Reward(
            title=reward.title,
            description=reward.description,
            points=reward.points,
            is_expiry_date=reward.is_expiry_date,
            valid_from=reward.valid_from,
            valid_till=reward.valid_till,
            employement_id=reward.employement_id
        )

        db.add(db_reward)
        db.commit()
        db.refresh(db_reward)
        return db_reward

    except SQLAlchemyError as e:
        return None


def update_reward(reward_id: str, reward: UpdateRewardSchema, db: Session) -> Any:
    """Update User"""

    try:

        db_user = db.query(Reward).filter(Reward.id == reward_id).first()

        db_user.title = reward.title,
        db_user.description = reward.description,
        db_user.points = reward.points,
        # db_user.is_expiry_date = reward.is_expiry_date,
        db_user.valid_from = reward.valid_from,
        db_user.valid_till = reward.valid_till,
        # db_user.employement_id = reward.employement_id

        db.commit()
        db.refresh(db_user)

        logger.info(db_user.points)

        return db_user

    except SQLAlchemyError as e:
        return None


def delete_reward(id: int, db: Session) -> Any:
    """Delete Reward"""
    try:
        db_user = db.query(Reward).filter(Reward.id == id).first()

        db_user.is_deleted = True
        db_user.deleted_at = datetime.now(timezone.utc)

        db.commit()
        db.refresh(db_user)

        return True
    except SQLAlchemyError as e:
        return None
