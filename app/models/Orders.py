from enum import Enum
from pydantic import BaseModel
import maya
from typing import Optional




class Status(str ,Enum):
    pending = 'pending'
    completed = 'completed'
    cancelled = 'cancelled'


class Order(BaseModel):
    id : Optional[int] = None
    user_id: Optional[int] = None
    status: Status = Status.pending
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class OrderUpdate(BaseModel):
    status: Status
    updated_at: Optional[str] = None