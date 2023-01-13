from sqlalchemy import (Boolean, Column, Date, DateTime, ForeignKey, Integer,
                        String, text)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.core.config import DATABASE_SCHEMA as schema
from app.core.models import *
from app.db.session import Base


class Reward(Base):
    __tablename__ = "rewards"
    __table_args__ = {"schema": schema}

    id = Column(
        UUID, primary_key=True, server_default=text("gen_random_uuid()")
    )
    title = Column(String(50), nullable=False, unique=True)
    description = Column(String(255))
    employement_id = Column(
        ForeignKey(f"{schema}.employements.id"), nullable=False
    )
    points = Column(Integer, nullable=False, server_default=text("0"))
    is_expiry_date = Column(
        Boolean, nullable=False, server_default=text("false")
    )
    valid_from = Column(Date, nullable=False)
    valid_till = Column(Date)
    created_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )
    is_deleted = Column(Boolean, nullable=False, server_default=text("false"))
    deleted_at = Column(DateTime(True))

    employement = relationship("Employement")
