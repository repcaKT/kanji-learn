from typing_extensions import final
import fastapi
import jwt
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import func
from sqlalchemy.sql.functions import mode
import database as local_db
from sqlalchemy import orm
from passlib import hash
from fastapi import Depends, security

import models
import schemas

# TODO change location of this secret
JWT_SECRET = "secretjwt"
oauth2schema = security.OAuth2PasswordBearer(tokenUrl="/api/token")


def create_database():
    return local_db.Base.metadata.create_all(bind=local_db.engine)


def get_db():
    db = local_db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_by_email(email: str, db: orm.Session):
    return db.query(models.User).filter(models.User.email == email).first()


async def create_user(user: schemas.UserCreate, db: orm.Session):
    user_obj = models.User(
        email=user.email,
        nickname=user.nickname,
        user_password=hash.bcrypt.hash(user.user_password),
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


async def authenticate_user(email: str, password: str, db: orm.Session):
    user = await get_user_by_email(db=db, email=email)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user


async def create_token(user: models.User):
    user_obj = schemas.User.from_orm(user)

    token = jwt.encode(user_obj.dict(), JWT_SECRET)

    return dict(access_token=token, token_type="bearer")


async def get_current_user(
    db: Session = fastapi.Depends(get_db), token: str = Depends(oauth2schema)
):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = db.query(models.User).get(payload["id"])
    except:
        raise fastapi.HTTPException(status_code=401, detail="Invalid Email or Password")
    return schemas.User.from_orm(user)

async def get_vocabulary_by_level(level: int,learnign_type: str,  db: orm.Session, user_id: int):
    result = db.query(models.Vocabulary).filter(models.Vocabulary.level == level).order_by(func.random()).limit(10).all()
    for element in result:
        incorrect_answers = db.query(models.Vocabulary).filter(models.Vocabulary.reading != element.reading).order_by(func.random()).limit(3).all()
        element.__dict__[f"{user_id}incorrect_answers"] = [answer.reading for answer in incorrect_answers]
    
    return {"questions":result}