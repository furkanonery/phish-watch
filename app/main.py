from fastapi import FastAPI
from app.views import user, phish
from app.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(phish.router)