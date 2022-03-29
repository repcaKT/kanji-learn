from fastapi import FastAPI
import fastapi as _fastapi
from fastapi import security
import fastapi
from sqlalchemy import orm
from sqlalchemy.sql.functions import user
import database as local_db
from fastapi.middleware.cors import CORSMiddleware

import httpx
import asyncio
import urllib.request, json 
import services
import schemas

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/users")
async def create_user(
    user: schemas.UserCreate, db: orm.Session = _fastapi.Depends(services.get_db)
):
    db_user = await services.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already in use")

    user = await services.create_user(user, db)
    return await services.create_token(user)


@app.post("/api/token")
async def generate_token(
    form_data: security.OAuth2PasswordRequestForm = _fastapi.Depends(),
    db: orm.Session = _fastapi.Depends(services.get_db),
):
    user = await services.authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid Credentials")

    return await services.create_token(user)


@app.get("/api/users/me", response_model=schemas.User)
async def get_user(user: schemas.User = _fastapi.Depends(services.get_current_user)):
    return user


@app.get("/api")
async def root():
    return {"message": "awesome Kanji app"}


@app.get("/quiz/{level}/{learnign_type}/{user_id}")
async def get_vocab(level,learnign_type,user_id, db: orm.Session = _fastapi.Depends(services.get_db)):
    result = await services.get_vocabulary_by_level(level, learnign_type, db, user_id)
    return result

@app.post("/api/currentprogress")
async def get_current_progress(data: dict,  db: orm.Session = _fastapi.Depends(services.get_db)):
    # result = await services.get_progress_by_id()
    return {"progress":[
    { "name": "N5", "learned": 100 },
    { "name": "N4", "learned": 70 },
    { "name": "N3", "learned": 40 },
    { "name": "N2", "learned": 20 },
    { "name": "N1", "learned": 100 },
  ]}
