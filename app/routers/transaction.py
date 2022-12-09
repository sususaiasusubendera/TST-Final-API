from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import oauth2, schemas, database
from sqlalchemy.orm import Session   
from ..repository import transaction


router = APIRouter(
    prefix="/transaction",
    tags=['Transactions']
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowTransaction])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return transaction.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Transaction, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return transaction.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return transaction.destroy(id, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowTransaction)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return transaction.show(id, db)