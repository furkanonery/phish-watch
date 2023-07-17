from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from ..database import engine

Base = declarative_base()

class PhishData(Base):
    __tablename__ = "phish_data"

    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String, unique=True)
    phish_url = Column(String)
    submitted_by = Column(String)
    is_valid = Column(String)
    is_online = Column(String)

Base.metadata.create_all(engine)