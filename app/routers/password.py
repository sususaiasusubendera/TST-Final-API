from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import oauth2, schemas, database
from sqlalchemy.orm import Session   
from ..repository import password


router = APIRouter(
    prefix="/password",
    tags=['Passwords']
)
get_db = database.get_db


@router.get('/')
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return password.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Password, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return password.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return password.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Password, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return password.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowPassword)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return password.show(id, db)