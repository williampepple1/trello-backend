from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class BoardBase(BaseModel):
    name: str

class BoardCreate(BoardBase):
    pass

class Board(BoardBase):
    id: int
    lists: list

    class Config:
        from_attributes = True

class ListBase(BaseModel):
    name: str

class ListCreate(ListBase):
    board_id: int

class List(ListBase):
    id: int
    cards: list

    class Config:
        from_attributes = True

class CardBase(BaseModel):
    title: str
    description: str

class CardCreate(CardBase):
    list_id: int

class Card(CardBase):
    id: int

    class Config:
        from_attributes = True
