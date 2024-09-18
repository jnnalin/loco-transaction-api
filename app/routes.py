from collections import deque

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Transaction as DBTransaction
from app.schemas import TransactionCreate, Transaction, TransactionSum, TransactionList

router = APIRouter()


@router.put("/transaction/{transaction_id}", response_model=dict)
async def create_transaction(transaction_id: int, transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = DBTransaction(id=transaction_id,
                                   amount=transaction.amount,
                                   type=transaction.type,
                                   parent_id=transaction.parent_id)
    db.add(db_transaction)
    db.commit()
    return {"status": "ok"}


@router.get("/transaction/{transaction_id}", response_model=Transaction)
async def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(DBTransaction).filter(DBTransaction.id == transaction_id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.get("/types/{type}", response_model=TransactionList)
async def get_transactions_by_type(type: str, db: Session = Depends(get_db)):
    transactions = db.query(DBTransaction).filter(DBTransaction.type == type).all()
    return TransactionList(transactions=[t.id for t in transactions])

