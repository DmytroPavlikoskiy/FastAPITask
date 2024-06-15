
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, default='user')


class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    username = Column(String, nullable=True)
    user_role = Column(String, nullable=False)
    bot_token = Column(String, nullable=False)
    chat_id = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    telegram_response = Column(Text, nullable=True)
    user = relationship("User")
