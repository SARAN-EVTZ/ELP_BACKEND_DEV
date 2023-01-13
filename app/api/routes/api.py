from fastapi import APIRouter, status
from loguru import logger

from app.core import config
from app.db.schema import HealthResponseSchema
from app.db.utils import ping_db


from app.reward import controller as reward_controller
from app.sample import controller as sample_controller
from app.user import controller as user_controller
from app.core import controller as core_controller
from app.dashboard import controller as dashboard_controller

router = APIRouter()


@router.get(
    "/health/",
    status_code=status.HTTP_200_OK,
    response_model=HealthResponseSchema,
)
async def root():
    try:
        ping_db()
    except Exception as ex:
        logger.exception("Health Check failed for DB.")
        db_status = f"ERROR: {ex}"

    else:
        db_status = "OK"

    status = {"db": db_status}
    return status


router.include_router(
    sample_controller.router, tags=["sample"], prefix="/sample"
)

router.include_router(user_controller.router, tags=["user"], prefix="/user")

router.include_router(
    reward_controller.router, tags=["reward"], prefix="/reward"
)


router.include_router(
    core_controller.router, tags=["core"], prefix="/core"
)


router.include_router(
    dashboard_controller.router, tags=["dashboard"], prefix="/dashbaord"
)
