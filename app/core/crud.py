from datetime import datetime, timezone
from typing import Any

from fastapi import HTTPException
from loguru import logger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.models import Group, Employement, Mode


def get_all_groups(db: Session):
    try:

        return db.query(Group).all()

    except SQLAlchemyError as e:
        return None


def get_all_employements(db: Session):
    try:

        return db.query(Employement).all()

    except SQLAlchemyError as e:
        return None


def get_all_modes(db: Session):
    try:

        return db.query(Mode).all()

    except SQLAlchemyError as e:
        return None
