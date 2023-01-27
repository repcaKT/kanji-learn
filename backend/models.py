import sqlalchemy
import passlib.hash as _hash

import database as _database


class User(_database.Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    nickname = sqlalchemy.Column(sqlalchemy.String(16), index=True)
    email = sqlalchemy.Column(sqlalchemy.String(50), unique=True, index=True)
    user_password = sqlalchemy.Column(sqlalchemy.String(50))

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.user_password)


class Vocabulary(_database.Base):
    __tablename__="vocabulary"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    kanji = sqlalchemy.Column(sqlalchemy.String(16), index=True)
    reading = sqlalchemy.Column(sqlalchemy.String(50), index=True)
    translation = sqlalchemy.Column(sqlalchemy.String(50))
    level = sqlalchemy.Column(sqlalchemy.String(16), index=True)
    times_learned = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
 
 
class Sentences(_database.Base):
    __tablename__="sentences"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    word = sqlalchemy.Column(sqlalchemy.String(16), index=True)
    sentence = sqlalchemy.Column(sqlalchemy.String(100))
    correct_answer = sqlalchemy.Column(sqlalchemy.String(50), index=True)
    bad_answers = sqlalchemy.Column(sqlalchemy.String(50))
    translation = sqlalchemy.Column(sqlalchemy.String(50))
    level = sqlalchemy.Column(sqlalchemy.String(16), index=True)
    times_learned = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))

    # word;sentence;correct_answer;bad_answers;translation;level