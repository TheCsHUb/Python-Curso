from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class ClientBase(BaseModel):
    name: str
    code: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    created_at_time: datetime

    class Config:
        orm_mode = True

class FoodOrderBase(BaseModel):
    client_id: int
    food_name: str

class FoodOrderCreate(FoodOrderBase):
    pass

class FoodOrderUpdate(BaseModel):
    client_id: Optional[int] = None
    food_name: Optional[str] = None

class FoodOrder(FoodOrderBase):
    id: int
    created_at_time: datetime

    class Config:
        orm_mode = True