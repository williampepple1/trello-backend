# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, models, db

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(db.get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(db.get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/boards/", response_model=schemas.Board)
def create_board(board: schemas.BoardCreate, db: Session = Depends(db.get_db), user_id: int = 1):  # For simplicity, assuming user_id = 1
    return crud.create_board(db=db, board=board, user_id=user_id)

@router.get("/boards/", response_model=list[schemas.Board])
def read_boards(db: Session = Depends(db.get_db), user_id: int = 1):  # Assuming user_id = 1
    return crud.get_boards(db=db, user_id=user_id)

@router.post("/lists/", response_model=schemas.List)
def create_list(list_: schemas.ListCreate, db: Session = Depends(db.get_db)):
    return crud.create_list(db=db, list_=list_)

@router.post("/cards/", response_model=schemas.Card)
def create_card(card: schemas.CardCreate, db: Session = Depends(db.get_db)):
    return crud.create_card(db=db, card=card)

@router.get("/lists/{list_id}/cards/", response_model=list[schemas.Card])
def read_cards(list_id: int, db: Session = Depends(db.get_db)):
    return crud.get_cards(db=db, list_id=list_id)
