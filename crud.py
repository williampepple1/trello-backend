
# crud.py
from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password  # Add hashing logic here
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_board(db: Session, board: schemas.BoardCreate, user_id: int):
    db_board = models.Board(name=board.name)
    db.add(db_board)
    db.commit()
    db.refresh(db_board)

    # Add the user to the board's membership
    membership = models.Membership(user_id=user_id, board_id=db_board.id)
    db.add(membership)
    db.commit()
    return db_board

def get_boards(db: Session, user_id: int):
    return db.query(models.Board).join(models.Membership).filter(models.Membership.user_id == user_id).all()

def create_list(db: Session, list_: schemas.ListCreate):
    db_list = models.List(name=list_.name, board_id=list_.board_id)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list

def create_card(db: Session, card: schemas.CardCreate):
    db_card = models.Card(title=card.title, description=card.description, list_id=card.list_id)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

def get_cards(db: Session, list_id: int):
    return db.query(models.Card).filter(models.Card.list_id == list_id).all()
