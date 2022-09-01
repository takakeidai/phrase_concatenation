from contextlib import contextmanager

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

# モデルベースクラスの作成
Base = declarative_base()

# SQL用のエンジンを作成
engine = create_engine('sqlite:///word_extension.sql')

Session = scoped_session(sessionmaker(bind=engine))

@contextmanager
def session_scope():
    session = Session()
    session.expire_on_commit = False
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise 
    finally:
        session.expire_on_commit = True
        session.close()

#v テーブル作成
class Word_Extension():
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String(255))
    created_word = sqlalchemy.Column(sqlalchemy.String(255))

# おはようテーブル
class Ohayou(Word_Extension, Base):
    __tablename__ = 'Ohayo'

# おやすみテーブル
class Oyasumi(Word_Extension, Base):
    __tablename__ = 'Oyasumi'

# ごめんねテーブル
class Gomenne(Word_Extension, Base):
    __tablename__ = 'Gomenne'

# おつかれテーブル
class Otsukare(Word_Extension, Base):
    __tablename__ = 'Otsukare'

def init_db():
    Base.metadata.create_all(bind=engine)
    
# end of line break
