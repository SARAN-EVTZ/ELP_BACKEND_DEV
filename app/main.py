import os

import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import Page, add_pagination, paginate
from loguru import logger
from pydantic import BaseModel
from starlette.requests import Request

from app.api.routes.api import router as api_router
from app.core import config
from app.db.session import SessionLocal

app = FastAPI(
    title=config.PROJECT_NAME,
    description=config.DESCRIPTION,


    contact={
        "name": ": Hemant Kumar Angajala",
        # "url": "http://x-force.example.com/contact/",
        "email": "hemant.angajala@evolutyz.com",
    },



    docs_url=f"{config.API_V1_STR}/docs",
    redoc_url=f"{config.API_V1_STR}/redoc",
    openapi_url= f"{config.API_V1_STR}/openapi.json",

)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8080",
    "http://localhost:3000",
    # "https://converter.swagger.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    logger.info("[STARTED]")


app.include_router(api_router, prefix=f"{config.API_V1_STR}")


@app.on_event("shutdown")
def shutdown_event():
    logger.info("[ENDED]")


add_pagination(app)


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", reload=True, port=8888)
