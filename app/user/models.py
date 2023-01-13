from sqlalchemy import (Boolean, Column, Date, DateTime, ForeignKey, Integer,
                        String, text, Text)
from sqlalchemy.dialects.postgresql import UUID


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.core.config import DATABASE_SCHEMA as schema
from app.core.models import *
from app.db.session import Base
from app.reward.models import *


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": schema}

    id = Column(
        UUID, primary_key=True, server_default=text("gen_random_uuid()")
    )
    employee_id = Column(String(10), unique=True)
    email_id = Column(String(255), nullable=False, unique=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(15))
    dob = Column(Date, nullable=False)
    gender = Column(String(2))
    designation = Column(String(15))
    group_id = Column(ForeignKey(f"{schema}.groups.id"), nullable=False)
    employement_id = Column(
        ForeignKey(f"{schema}.employements.id"), nullable=False
    )
    created_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )
    is_deleted = Column(Boolean, nullable=False, server_default=text("false"))
    deleted_at = Column(DateTime(True))

    employement = relationship("Employement")
    group = relationship("Group")


class UserReward(Base):
    __tablename__ = "user_rewards"
    __table_args__ = {"schema": schema}

    id = Column(
        UUID, primary_key=True, server_default=text("gen_random_uuid()")
    )
    user_id = Column(ForeignKey(f"{schema}.users.id"), nullable=False)
    reward_id = Column(ForeignKey(f"{schema}.rewards.id"), nullable=False)

    comment = Column(Text)
    citation_id = Column(ForeignKey(f"{schema}.users.id"), nullable=False)
    certificate = Column(Text)
    is_uploaded = Column(Boolean, nullable=False, server_default=text("false"))

    created_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )

    citation = relationship(
        'User', primaryjoin='UserReward.citation_id == User.id')
    reward = relationship('Reward')
    user = relationship('User', primaryjoin='UserReward.user_id == User.id')
