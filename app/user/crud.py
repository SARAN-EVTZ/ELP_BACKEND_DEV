from datetime import datetime, timezone
from typing import Any

from fastapi import HTTPException
from loguru import logger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from sqlalchemy import or_


from app.user.models import User, UserReward
from app.user.schema import CreateUserSchema, SchemaAssignReward

# class UserFound(Exception):
#     def __init__(self, message):
#         self.message = message

#         super().__init__(message)

#     def __str__(self):
#         return self.message


def get_users_from_db(db: Session):

    try:

        return db.query(User).filter(User.is_deleted == False).all()

    except SQLAlchemyError as e:
        return None


def get_me_from_db(db: Session, id):

    _user = db.query(User).filter(User.id == id).first()

    if _user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return _user


def get_user(db: Session, email_id, employee_id) -> Any:
    """Get User Data based on email"""

    try:
        return db.query(User).filter(User.employee_id == employee_id).first()

    except SQLAlchemyError as e:
        logger.exception("get_user")
        return None


def create_user(db: Session, user: CreateUserSchema) -> Any:
    """Add New User"""
    try:

        db_user = User(
            employee_id=user.employee_id,
            email_id=user.email_id,
            first_name=user.first_name,
            last_name=user.last_name,
            phone_number=user.phone_number,
            dob=user.dob,
            gender=user.gender,
            designation=user.designation,
            group_id=user.group_id,
            employement_id=user.employement_id,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    except SQLAlchemyError as e:
        return None


def update_user(user_id: int, user: CreateUserSchema, db: Session) -> Any:
    """Update User"""
    try:
        db_user = db.query(User).filter(User.id == user_id).first()

        db_user.employee_id = user.employee_id
        db_user.email_id = user.email_id
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.phone_number = user.phone_number
        db_user.dob = user.dob
        db_user.gender = user.gender
        db_user.designation = user.designation
        db_user.group_id = user.group_id
        db_user.employement_id = user.employement_id

        db.commit()
        db.refresh(db_user)

        return db_user

    except SQLAlchemyError as e:
        return None


def delete_user(id: int, db: Session) -> Any:
    """Delete User"""
    try:
        db_user = db.query(User).filter(User.id == user_id).first()

        db_user.is_deleted = True
        db_user.deleted_at = datetime.now(timezone.utc)

        db.commit()
        db.refresh(db_user)

        return True
    except SQLAlchemyError as e:
        return None


def create_user_reward(db: Session, details: SchemaAssignReward):
    """assign New reward to User"""

    try:

        db_user_reward = UserReward(
            user_id=details.user_id,
            reward_id=details.reward_id,
            comment=details.comment,
            citation_id=details.citation_id,
            certificate=details.certificate,
            is_uploaded=details.is_uploaded
        )

        db.add(db_user_reward)
        db.commit()
        db.refresh(db_user_reward)
        return db_user_reward

    except SQLAlchemyError as e:
        return None
