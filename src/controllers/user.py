from sqlalchemy.orm import Session
from src.schemas.user import UserCreate
from src.models.user import User as UserModel
from typing import List
from fastapi import HTTPException

def create_user(user: UserCreate, db: Session) -> UserModel:
    db_user = UserModel(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db: Session) -> List[UserModel]:
    users = db.query(UserModel).all()
    return users

def get_user(user_id: int, db: Session) -> UserModel | HTTPException:
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user