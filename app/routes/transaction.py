from collections import deque

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from db.postgres import get_db
from models.schema import Transaction as DBTransaction
from models.pydantic import TransactionCreate, Transaction, TransactionSum, TransactionList

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


@router.get("/sum/{transaction_id}", response_model=TransactionSum)
async def get_transaction_sum(transaction_id: int, db: Session = Depends(get_db)):

    def calculate_sum(trans_id):
        total_sum = 0.0
        visited = set()  # Tracking visited transactions to avoid duplicates

        children_transactions = deque()

        # Get the first list of child transactions of the given trans_id
        # considering the given trans_id as the parent_id
        initial_transactions = db.query(DBTransaction).filter(DBTransaction.parent_id == trans_id).all()
        for t in initial_transactions:
            children_transactions.append((t.id, t.amount))

        # Process the children_transactions
        while children_transactions:
            # Get the next transaction to process
            current_id, current_amount = children_transactions.popleft()

            # If this transaction was already visited, skip it
            if current_id in visited:
                continue

            # Add the transaction's amount to the total sum
            total_sum += current_amount

            # Mark this transaction as visited
            visited.add(current_id)

            # Find all child transactions of the current transaction
            child_transactions = db.query(DBTransaction).filter(DBTransaction.parent_id == current_id).all()

            # Add child transactions to the children_transactions for further processing
            for t in child_transactions:
                if t.id not in visited:  # Only add if not visited
                    children_transactions.append((t.id, t.amount))

        return total_sum

    # Get the sum of amount for all the child transactions
    total_amount = calculate_sum(transaction_id)

    return TransactionSum(sum=total_amount)
