from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas.user import User, UserCreate, UserBase
from ..models.user import User as UserModel
from ..database import get_db
from typing import List
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.post("/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users", response_model=List[User])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user