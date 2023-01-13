from app.db.session import Base
from app.core.config import DATABASE_SCHEMA as schema

from sqlalchemy import (Boolean, Column, Date, DateTime, ForeignKey, Integer,
                        String, text)
from sqlalchemy.dialects.postgresql import UUID


class Banner(Base):
    __tablename__ = "banners"
    __table_args__ = {"schema": schema}

    id = Column(
        UUID, primary_key=True, server_default=text("gen_random_uuid()")
    )

    title = Column(String(50), nullable=False, unique=True)
    image = Column(String(), nullable=False, unique=True)
    start_date = Column(Date)
    end_date = Column(Date)

    created_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )

    updated_at = Column(
        DateTime(True), server_default=text("CURRENT_TIMESTAMP")
    )

    is_deleted = Column(Boolean, nullable=False, server_default=text("false"))
    deleted_at = Column(DateTime(True))
