from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from src.database import engine

Base = declarative_base()

class PhishData(Base):
    __tablename__ = "phish_data"

    id = Column(Integer, primary_key=True, index=True)
    phish_id = Column(String, unique=True)
    url = Column(String)
    verified = Column(String)
    online = Column(String)
    submission_time = Column(DateTime)
    verification_time = Column(DateTime)

Base.metadata.create_all(engine)