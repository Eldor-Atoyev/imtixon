from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://eldoratoyev:pass@localhost/mydb", echo=True)

Base = declarative_base()
metadata = Base.metadata
Session = sessionmaker(bind=engine)


class User(Base):
    tablename = 'users'
    id = Column(Integer, primary_key=True)
    user_telegram_id = Column(String, unique=True)
    username = Column(String)
    created = Column(DateTime)


class Message_(Base):
    tablename = 'usermessage'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    text = Column(String)
    created = Column(DateTime)


Base.metadata.create_all(engine)