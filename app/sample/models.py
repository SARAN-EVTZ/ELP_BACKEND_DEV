from sqlalchemy import JSON, TIMESTAMP, Column, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import DATABASE_SCHEMA as schema
from app.db.session import Base


class Student(Base):

    __tablename__ = "student"
    __table_args__ = {"schema": schema}

    id = Column(INTEGER(11), primary_key=True)
    enroll = Column(INTEGER(11))
    personal_info = Column(JSON)
    name = Column(String(255))
    created_on = Column(
        TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
