from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas.user import User, UserCreate
from src.database import get_db
from src.controllers.user import create_user, get_all_users, get_user

router = APIRouter()

@router.post("/users", response_model=User)
def create_user_view(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)

@router.get("/users", response_model=List[User])
def get_all_users_view(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/users/{user_id}", response_model=User)
def get_user_view(user_id: int, db: Session = Depends(get_db)):
    return get_user(user_id, db)