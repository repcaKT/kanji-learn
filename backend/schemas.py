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
    times_learned: int

class VocabCreate(_VocabularyBase):
    user_id: int
    class Config:
        orm_mode = True

class Vocabulary(_VocabularyBase):
    id: int
    
    class Config:
        orm_mode =True


class _SentencesBase(BaseModel):
    word: str
    sentence: str
    correct_answer: str
    bad_answers: str
    translation: str
    level: str
    times_learned: int

class SentencesCreate(_SentencesBase):
    user_id: int
    class Config:
        orm_mode = True

class Sentences(_SentencesBase):
    id: int
    
    class Config:
        orm_mode =True


# word = sqlalchemy.Column(sqlalchemy.String(16), index=True)
#     sentence = sqlalchemy.Column(sqlalchemy.String(100))
#     correct_answer = sqlalchemy.Column(sqlalchemy.String(50), index=True)
#     bad_answers = sqlalchemy.Column(sqlalchemy.String(50), index=True)
#     translation = sqlalchemy.Column(sqlalchemy.String(50), index=True)
#     level = sqlalchemy.Column(sqlalchemy.String(16), index=True)
#     times_learned = sqlalchemy.Column(sqlalchemy.Integer, index=True)
#     user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
