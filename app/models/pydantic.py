from pydantic import BaseModel
from typing import Optional


class TransactionBase(BaseModel):
    amount: float
    type: str
    parent_id: Optional[int] = None


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True


class TransactionList(BaseModel):
    transactions: list[int]


class TransactionSum(BaseModel):
    sum: float
