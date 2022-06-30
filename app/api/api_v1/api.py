from fastapi import APIRouter

from .endpoints import (
    users,
    utils,
    measurements,
    orders,
)


router = APIRouter()


router.include_router(users.router, prefix='/users', tags=['Users'])
router.include_router(measurements.router, prefix='/measurement', tags=['Measurements'])
router.include_router(orders.router, prefix='/orders', tags=['Orders'])
router.include_router(utils.router)

