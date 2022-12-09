from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from datetime import datetime

def get_all(db: Session):
    transaction = db.query(models.Transaction).all()
    return transaction

# Core
def create(request: schemas.Transaction, db: Session):
    now = datetime.now()
    today = now.strftime("%w")
    pword_today = db.query(models.Password.pword).filter(models.Password.day == today)
    new_transaction = models.Transaction(ordered_menus=request.ordered_menus, total_price=request.total_price, date=request.date, pword_avail=pword_today)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

def destroy(id: int, db: Session):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id)
    if not transaction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Transaction with id {id} not found')
    transaction.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schemas.Transaction, db: Session):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id)
    if not transaction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Transaction with id {id} not found')
    transaction.update(request.dict())
    db.commit()
    return 'updated'

def show(id: int, db: Session):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Transaction with the id {id} is not available')
    return transaction