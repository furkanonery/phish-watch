from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas.phish import PhishData, PhishDataCreate
from src.database import get_db
from src.controllers.phish import create_phish_data, get_all_phish_data, get_phish
from src.tasks.phish_tank import get_phish

router = APIRouter()

@router.post("/phish", response_model=PhishData)
def create_phish_view(phish: PhishDataCreate, db: Session = Depends(get_db)):
    
    return create_phish_data(phish, db)

@router.get("/phish", response_model=List[PhishData])
def get_all_phish_view(db: Session = Depends(get_db)):
    
    return get_all_phish_data(db)

@router.get("/phish/{phish_id}", response_model=PhishData)
def get_phish_view(phish_id: int, db: Session = Depends(get_db)):

    return get_phish(phish_id, db)