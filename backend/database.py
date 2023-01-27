import sqlalchemy
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# DATABASE_URL = "sqlite"

engine = sqlalchemy.create_engine("mysql+pymysql://root:@127.0.0.1:3306/kanji_learn")
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = _declarative.declarative_base()
engine.connect()
