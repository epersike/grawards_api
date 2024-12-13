from fastapi import FastAPI

from contextlib import asynccontextmanager
import toml

from app.schemas import IntervalsResponse
from app.db import initialize_database
from app.controllers import read_movies_from_db, calculate_intervals

@asynccontextmanager
async def lifespan(app: FastAPI):
    '''
        Context manager to initialize the database.
    '''
    initialize_database()
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get("/intervals", response_model=IntervalsResponse)
def get_intervals():
    '''
        Get the minimum and maximum intervals between wins for producers.
    '''
    data = read_movies_from_db()
    intervals = calculate_intervals(data)
    return intervals

@app.get("/")
def root():
    '''
        Root endpoint to check if API is online and it's version.
    '''
    pyproject = toml.load("app/pyproject.toml")
    version = pyproject["project"]["version"]
    return {"message": "ok", "version": version}