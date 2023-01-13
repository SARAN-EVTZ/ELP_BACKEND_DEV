from sqlalchemy import (Boolean, Column, Date, DateTime, ForeignKey, Integer,
                        String, text)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.core.config import DATABASE_SCHEMA as schema
from app.db.session import Base
from app.reward.models import *


class Employement(Base):
    __tablename__ = "employements"
    __table_args__ = {"schema": schema}

    id = Column(
        UUID, primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255))
    created_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )
    is_deleted = Column(Boolean, nullable=False, server_default=text("false"))
    deleted_at = Column(DateTime(True))


class Group(Base):
    __tablename__ = "groups"
    __table_args__ = {"schema": schema}

    id = Column(
        UUID, primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255))
    created_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )
    is_deleted = Column(Boolean, nullable=False, server_default=text("false"))
    deleted_at = Column(DateTime(True))


class Mode(Base):
    __tablename__ = "modes"
    __table_args__ = {"schema": schema}

    id = Column(
        UUID, primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255))
    created_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )
    is_deleted = Column(Boolean, nullable=False, server_default=text("false"))
    deleted_at = Column(DateTime(True))


class EmployementReward(Base):
    __tablename__ = "employement_rewards"
    __table_args__ = {"schema": schema}

    id = Column(
        UUID, primary_key=True, server_default=text("gen_random_uuid()")
    )
    employement_id = Column(
        ForeignKey(f"{schema}.employements.id"), nullable=False
    )
    reward_id = Column(ForeignKey(f"{schema}.rewards.id"), nullable=False)
    created_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )

    employement = relationship("Employement")
    reward = relationship("Reward")
