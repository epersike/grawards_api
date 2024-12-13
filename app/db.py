import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.orm import Session

from app.models import Base, Movie

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

CSV_FILE = 'db/movielist.csv'

def initialize_database():
    '''
        Initializes the database reading the CSV file and inserting 
        the data formatted by models.
    '''
    init_db()
    db: Session = SessionLocal()
    if db.query(Movie).count() == 0:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                movie = Movie(
                    year=row['year'],
                    title=row['title'],
                    studios=row['studios'],
                    producers=row['producers'],
                    winner=row['winner']
                )
                db.add(movie)
        db.commit()
    db.close()