from pydantic import BaseModel

class PhishDataBase(BaseModel):
    identifier: str
    phish_url: str
    submitted_by: str
    is_valid: str
    is_online: str

    class Config:
        orm_mode = True

class PhishDataCreate(BaseModel):
    identifier: str
    phish_url: str
    submitted_by: str
    is_valid: str
    is_online: str

    class Config:
        orm_mode = True

class PhishData(BaseModel):
    id: int
    identifier: str
    phish_url: str
    submitted_by: str
    is_valid: str
    is_online: str

    class Config:
        orm_mode = True