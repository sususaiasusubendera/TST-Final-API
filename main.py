from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import password, transaction, user, authentication


app = FastAPI()


models.Base.metadata.create_all(engine)


app.include_router(password.router)
app.include_router(transaction.router)
app.include_router(user.router)
app.include_router(authentication.router)

@app.get('/')
def homepage():
    return 'Welcome'