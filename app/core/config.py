import os

PROJECT_NAME = "ELP Backend"

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Password@localhost:5432/ELPnew"




API_V1_STR = "/api/v1"

DATABASE_SCHEMA = "dev"

JWT_SECRET = "87198ce9dbb359cd7d70f882ee2189bf6dcbf75240b6f0c8"
JWT_ALGORITHM = "HS256"

DESCRIPTION = f"Evolutyz Loyality Program {DATABASE_SCHEMA.upper()} API helps you access royality program. 🚀"
