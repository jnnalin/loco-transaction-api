# loco-transaction-api
A FastAPI application for managing transactions stored in a PostgreSQL database. This service allows users the following features:

## Features

- Create transactions with an optional parent-child relationship.
- Retrieve transaction details by ID.
- List all transaction IDs of a specific type.
- Calculate the total amount of all linked transactions. (Parent-Child transactions)
- NOTE: For the `sum` API, I have assumed the given transaction_id in the request as parent_id to look for all child transaction ids and their subsequent children. 

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python
- **SQLAlchemy**: ORM for database interaction.
- **PostgreSQL**: Relational database management system.
- **Pydantic**: Data validation and settings management using Python type annotations.

### Installation
```
1.Create a virtual environment :
  python -m venv venv
  source venv/bin/activate

2.Install the required packages:
  pip install -r requirements.txt

3.Set up your PostgreSQL database and add the DATABASE_URL in the .env file present inside the app folder
  DATABASE_URL=postgresql://username:password@localhost:port/dbname

4.Run the application:
  cd app/
  uvicorn main:app --reload
```

### API Endpoints


- **Create a Transaction**: PUT /transactionservice/transaction/{transaction_id}
- **Retrieve a Transaction by ID**: GET /transactionservice/transaction/{transaction_id}
- **List Transactions by Type**: GET /transactionservice/types/{type}
- **Calculate the Sum of Linked Transaction**: GET /transactionservice/sum/{transaction_id}
