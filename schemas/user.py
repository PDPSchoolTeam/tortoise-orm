from pydantic import BaseModel
from datetime import datetime


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True


class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    user_id: int

    class Config:
        orm_mode = True
