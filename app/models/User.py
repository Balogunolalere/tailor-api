#from datetime import datetime
from pydantic import BaseModel, Field,EmailStr
from typing import Union, Optional
from datetime import datetime


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)
    email : EmailStr
    first_name : str = Field(..., min_length=3, max_length=50)
    last_name : str = Field(..., min_length=3, max_length=50)
    phone : str = Field(..., min_length=3, max_length=50)
    address : str = Field(..., min_length=3, max_length=200)
    city : str = Field(..., min_length=3, max_length=50)
    state : str = Field(..., min_length=3, max_length=50)
    zip : str = Field(..., min_length=3, max_length=50)
    country_code : str = Field(..., min_length=2, max_length=5)
    disabled : bool = False
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

     #validate phone number matches +23470xxxxxxxx
    def validate_phone_number(self):
        if self.phone[0:3] != '+234':
            raise ValueError('Phone number must start with +234')
        if len(self.phone) != 13:
            raise ValueError('Phone number must be 13 digits')
        if self.phone[3:13].isdigit() == False:
            raise ValueError('Phone number must be digits')
        return self.phone

    #validate zip code matches 100001
    def validate_zip_code(self):
        if len(self.zip) != 6:
            raise ValueError('Zip code must be 6 digits')
        if self.zip.isdigit() == False:
            raise ValueError('Zip code must be digits')
        return self.zip



class UserCreateResponse(BaseModel):
    username: Union[str, None] = None
    id : Union[str, None] = None
    email : Union[EmailStr, None] = None
    first_name : Union[str, None] = None
    last_name : Union[str, None] = None
    phone : Union[str, None] = None
    address : Union[str, None] = None
    city : Union[str, None] = None
    state : Union[str, None] = None
    zip : Union[str, None] = None
    country : Union[str, None] = None
    disabled : Union[bool, None] = None
    created_at : Union[str, None] = None



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    id : Union[str, None] = None
    username: str
    email: Union[EmailStr, None] = None
    disabled: Union[bool, None] = None



