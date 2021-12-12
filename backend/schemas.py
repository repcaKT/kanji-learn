import datetime
from pydantic import BaseModel


class _UserBase(BaseModel):
    email: str
    nickname: str


class UserCreate(_UserBase):
    user_password: str

    class Config:
        orm_mode = True


class User(_UserBase):
    id: int

    class Config:
        orm_mode = True
