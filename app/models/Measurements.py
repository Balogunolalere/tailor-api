from typing import Optional
from pydantic import BaseModel
import maya



class Measurement(BaseModel):
    id : Optional[int] = None
    user_id: Optional[int] = None
    shoulder: Optional[int] = None
    neck: Optional[int] = None
    chest: Optional[int] = None
    waist: Optional[int] = None
    sleeve: Optional[int] = None
    length: Optional[int] = None
    thighs: Optional[int] = None
    bust: Optional[int] = None
    length_trouser: Optional[int] = None
    length_shirt: Optional[int] = None
    length_blouse: Optional[int] = None
    length_skirt: Optional[int] = None
    length_full: Optional[int] = None
    hips: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    notes: Optional[str] = None

class MeasurementUpdate(BaseModel):
    shoulder: Optional[int] = None
    neck: Optional[int] = None
    chest: Optional[int] = None
    waist: Optional[int] = None
    sleeve: Optional[int] = None
    length: Optional[int] = None
    thighs: Optional[int] = None
    bust: Optional[int] = None
    length_trouser: Optional[int] = None
    length_shirt: Optional[int] = None
    length_blouse: Optional[int] = None
    length_skirt: Optional[int] = None
    length_full: Optional[int] = None
    hips: Optional[int] = None
    notes: Optional[str] = None
    updated_at: Optional[str] = None