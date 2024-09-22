from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

from db.postgres import init_db
from routes.transaction import router

app = FastAPI()

# Initialize the database when the application starts
init_db()

app.include_router(router, prefix="/transactionservice")
