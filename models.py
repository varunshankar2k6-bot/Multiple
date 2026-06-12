from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True)


class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    body = Column(String(500))
    user_id = Column(Integer, ForeignKey("users.id"))