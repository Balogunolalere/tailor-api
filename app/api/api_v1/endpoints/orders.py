from fastapi import APIRouter, Depends, HTTPException, status
from app.deps import get_current_active_user
from app.models.User import (
    User,
)
from app.models.Orders import (
    Order,
    OrderUpdate
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
async def create_order(request: Order = Depends(), current_user: User = Depends(get_current_active_user)):
    try:
        user = db.fetch({"username": current_user['username']}).items[0]
    except Exception:
        user = None
    try:
        id = user['orders']['id']
    except Exception:
        id = None
    if id is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has an order",
        )
    data = dict(request)
    data["id"] = str(uuid4())
    data["user_id"] = current_user['id']
    data["created_at"] = str(maya.now())
    data["updated_at"] = str(maya.now())
    db.update(
        {'orders' : data},
        str(user['key'])
    )
    return data

@router.get('/{id}/')
async def get_order(id: str, current_user: User = Depends(get_current_active_user)):
    
        try:
            order = db.fetch({'orders.id': id}).items[0]
        except Exception:
            order = None
        if order is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User does not have an order",
            )
        return order

@router.get('/all')
async def get_all_orders(current_user: User = Depends(get_current_active_user)):
    try:
        user = db.fetch({"username": current_user['username']}).items[0]
    except Exception:
        user = None
    if user['is_admin'] is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Forbidden",
        )
    resp = [ x['orders'] for x in db.fetch().items ]
    return resp
    
    


@router.patch('/{id}')
async def update_order(id: str, request: OrderUpdate = Depends(), current_user: User = Depends(get_current_active_user)):
    try:
        user = db.fetch({"username": current_user['username']}).items[0]
    except Exception:
        user = None
    try:
        order = db.fetch({'orders.id': id}).items[0]
    except Exception:
        order = None
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not have an order",
        )
    data = dict(request)
    data["updated_at"] = str(maya.now())
    db.update(
        {'orders' : data},
        str(user['key'])
    )
    return data

@router.delete('/{id}')
async def delete_order(id: str, current_user: User = Depends(get_current_active_user)):
    try:
        user = db.fetch({"username": current_user['username']}).items[0]
    except Exception:
        user = None
    try:
        order = db.fetch({'orders.id': id}).items[0]
    except Exception:
        order = None
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not have an order",
        )
    db.delete(
        str(user['key'])
    )
    return {'message': 'Order deleted'}