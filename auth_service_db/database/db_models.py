from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    nickname = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    rating = Column(Integer)
