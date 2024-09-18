# loco-transaction-api
A FastAPI application for managing transactions stored in a PostgreSQL database. This service allows users to create transactions, retrieve transaction details like get the the transaction details from transaction id and list of all transaction ids that share the same type and compute sums of linked transactions.

## Features

- Create transactions with an optional parent-child relationship.
- Retrieve transaction details by ID.
- List all transaction IDs of a specific type.
- Calculate the total amount of all linked transactions. (Parent-Child transactions)

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.6+.
- **SQLAlchemy**: ORM for database interaction.
- **PostgreSQL**: Relational database management system.
- **Pydantic**: Data validation and settings management using Python type annotations.

### Installation
```
1.Create a virtual environment :
  bash script
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`


2.Install the required packages:
  bash
  pip install -r requirements.txt

3.Set up your PostgreSQL database and update the .env file with your database credentials:
  text
  DATABASE_URL=postgresql://username:password@localhost/dbname

4.Run the application:
  bash
  uvicorn app.main:app --reload
```

### API Endpoints


- **Create a Transaction**: PUT /transactionservice/transaction/{transaction_id}
- **Retrieve a Transaction by ID**: GET /transactionservice/transaction/{transaction_id}
- **List Transactions by Type**: GET /transactionservice/types/{type}
- **Calculate the Sum of Linked Transaction**: GET /transactionservice/sum/{transaction_id}
