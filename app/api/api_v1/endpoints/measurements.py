from fastapi import APIRouter, Depends, HTTPException, status
from app.deps import get_current_active_user
from app.models.User import (
    User,
)
from app.models.Measurements import (
    Measurement,
    MeasurementUpdate
)
from uuid import uuid4

from secrets import (
    DETA_KEY,
)
from deta import Deta

import maya

deta = Deta(DETA_KEY)

db = deta.Base("tailor_users")






router = APIRouter()

@router.post('/create')
async def create_measurement(request: Measurement = Depends(), current_user: User = Depends(get_current_active_user)):
    try:
        user = db.fetch({"username": current_user['username']}).items[0]
    except Exception:
        user = None
    try:
        id = user['measurements']['id']
    except Exception:
        id = None
    if id is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has a measurement",
        )
    data = dict(request)
    data["id"] = str(uuid4())
    data["user_id"] = current_user['id']
    data["created_at"] = str(maya.now())
    data["updated_at"] = str(maya.now())
    db.update(
        {'measurements' : data},
        str(user['key'])
    )
    return data

@router.get('/{id}/')
async def get_measurement(id: str, current_user: User = Depends(get_current_active_user)):

    try:
        measurement = db.fetch({'measurements.id': id}).items[0]
    except Exception:
        measurement = None
    if measurement is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="must be admin",
        )
    return measurement['measurements']

@router.get('/all')
async def get_all_measurements(current_user: User = Depends(get_current_active_user)):
    try:
        user = db.fetch({"username": current_user['username']}).items[0]
    except Exception:
        user = None
    if user['is_admin'] is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Forbidden",
        )
    resp = [x['measurements'] for x in db.fetch().items ]
    return resp
    


@router.patch('/{id}')
async def update_measurement(id: str, request: MeasurementUpdate = Depends(), current_user: User = Depends(get_current_active_user)):
    try:
        user = db.fetch({"username": current_user['username']}).items[0]
    except Exception:
        user = None
    try:
        measurement = db.fetch({'measurements.id': id}).items[0]
    except Exception:
        measurement = None
    if measurement is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Measurement not found",
        )
    data = dict(request)
    data["updated_at"] = str(maya.now())
    db.update(
        {'measurements' : data},
        str(user['key'])
    )
    return data

@router.delete('/{id}')
async def delete_measurement(id: str, current_user: User = Depends(get_current_active_user)):
    try:
        user = db.fetch({"username": current_user['username']}).items[0]
    except Exception:
        user = None
    try:
        measurement = db.fetch({'measurements.id': id}).items[0]
    except Exception:
        measurement = None
    if measurement is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Measurement not found",
        )
    db.delete(
        str(user['key'])
    )
    return {'deleted': 'deleted'}
