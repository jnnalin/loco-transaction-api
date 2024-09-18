from fastapi import FastAPI
from app.db import init_db
from app.routes import router

app = FastAPI()

# Initialize the database when the application starts
init_db()

app.include_router(router, prefix="/transactionservice")
