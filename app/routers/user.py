from typing import List
from fastapi import APIRouter, Depends, status
from.. import database, schemas, oauth2
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowUser])
def all(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.destroy(id, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)