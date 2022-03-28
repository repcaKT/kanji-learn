import datetime
import sqlalchemy
import sqlalchemy.orm as _orm
import passlib.hash as _hash
from sqlalchemy.sql.functions import user

import database as _database


class User(_database.Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    nickname = sqlalchemy.Column(sqlalchemy.String(16), index=True)
    email = sqlalchemy.Column(sqlalchemy.String(50), unique=True, index=True)
    user_password = sqlalchemy.Column(sqlalchemy.String(50))

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.user_password)


class Vocabulary(_database.Base):
    __tablename__="vocabulary"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    kanji = sqlalchemy.Column(sqlalchemy.String(16), index=True)
    reading = sqlalchemy.Column(sqlalchemy.String(50), index=True)
    translation = sqlalchemy.Column(sqlalchemy.String(50), index=True)
    level = sqlalchemy.Column(sqlalchemy.String(16), index=True)
    times_learned = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
 