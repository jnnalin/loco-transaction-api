from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from db.postgres import Base


# Define Transactions table model
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)
    parent_id = Column(Integer, ForeignKey('transactions.id'))

    parent = relationship("Transaction", remote_side=[id], backref="children")
