import sqlalchemy

##create tables
#db
    #users
    #posts
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker    

db_url = "sqlite:///test.db"
engine = create_engine(db_url)


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    off_name = Column(String)
    user_name = Column(String)

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    caption = Column(String)
    photo_url = Column(String)

Base.metadata.create_all(engine)

##create session
Session = sessionmaker(bind=engine)
session = Session()

mercy = User(off_name = "mercy njoki",user_name = "broenie")
session.add(mercy)
session.commit()
