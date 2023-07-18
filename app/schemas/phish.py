from pydantic import BaseModel
from datetime import datetime

class PhishDataBase(BaseModel):
    phish_id: str
    url: str
    verified: str
    online: str
    submission_time: datetime
    verification_time: datetime

    class Config:
        orm_mode = True

class PhishDataCreate(BaseModel):
    phish_id: str
    url: str
    verified: str
    online: str
    submission_time: datetime
    verification_time: datetime

    class Config:
        orm_mode = True

class PhishData(BaseModel):
    id: int
    phish_id: str
    url: str
    verified: str
    online: str
    submission_time: datetime
    verification_time: datetime

    class Config:
        orm_mode = True