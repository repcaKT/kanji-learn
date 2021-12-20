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

class _VocabularyBase(BaseModel):
    kanji: str
    reading: str
    translation: str
    level: str

class VocabCreate(_VocabularyBase):
    user_id: int
    class Config:
        orm_mode = True

class Vocabulary(_VocabularyBase):
    id: int
    
    class Config:
        orm_mode =True