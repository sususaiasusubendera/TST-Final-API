from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    password = db.query(models.Password).all()
    return password

def create(request: schemas.Password, db: Session):
    new_password = models.Password(pword=request.pword, day=request.day)
    db.add(new_password)
    db.commit()
    db.refresh(new_password)
    return new_password

def destroy(id: int, db: Session):
    password = db.query(models.Password).filter(models.Password.id == id)
    if not password.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Password with id {id} not found')
    password.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schemas.Password, db: Session):
    password = db.query(models.Password).filter(models.Password.id == id)
    if not password.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Password with id {id} not found')
    password.update(request.dict())
    db.commit()
    return 'updated'

def show(id: int, db: Session):
    password = db.query(models.Password).filter(models.Password.id == id).first()
    if not password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Password with the id {id} is not available')
    return password