from sqlalchemy.orm import Session
from ..schemas.phish import PhishDataCreate
from ..models.phish import PhishData as PhishDataModel
from typing import List
from fastapi import HTTPException
from sqlalchemy import exc


def create_phish_data(phish: PhishDataCreate, db: Session):
    db_phish_data = PhishDataModel(identifier=phish.identifier,
                                   phish_url=phish.phish_url,
                                   submitted_by=phish.submitted_by,
                                   is_valid=phish.is_valid,
                                   is_online=phish.is_online)
    try:
    # Yeni veriyi veritabanına kaydetme işlemi
        db.add(db_phish_data)
        db.commit()
    except exc.IntegrityError as e:
    # Hata alındığında işlemleri geri al
        db.rollback()
    db.refresh(db_phish_data)
    return db_phish_data


def get_all_phish_data(db: Session) -> List[PhishDataModel]:
    phish_data = db.query(PhishDataModel).all()
    return phish_data


def get_phish(phish_id: int, db: Session):
    db_phish_data = db.query(PhishDataModel).filter(PhishDataModel.id == phish_id).first()
    if not db_phish_data:
        raise HTTPException(status_code=404, detail="Phish data not found")
    return db_phish_data
