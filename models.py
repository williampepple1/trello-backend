from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    boards = relationship("Board", secondary="membership")

class Board(Base):
    __tablename__ = 'boards'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    lists = relationship("List", back_populates="board")

class List(Base):
    __tablename__ = 'lists'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    board_id = Column(Integer, ForeignKey('boards.id'))
    board = relationship("Board", back_populates="lists")
    cards = relationship("Card", back_populates="list")

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String, nullable=True)
    list_id = Column(Integer, ForeignKey('lists.id'))
    list = relationship("List", back_populates="cards")

class Membership(Base):
    __tablename__ = 'membership'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    board_id = Column(Integer, ForeignKey('boards.id'), primary_key=True)
