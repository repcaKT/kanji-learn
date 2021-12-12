import datetime
import sqlalchemy
import sqlalchemy.orm as _orm
import passlib.hash as _hash

import database as _database


class User(_database.Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    nickname = sqlalchemy.Column(sqlalchemy.String(16), index=True)
    email = sqlalchemy.Column(sqlalchemy.String(50), unique=True, index=True)
    user_password = sqlalchemy.Column(sqlalchemy.String(50))

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.user_password)
