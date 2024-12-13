from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, index=True)
    title = Column(String, index=True)
    studios = Column(String, index=True)
    producers = Column(String, index=True)
    winner = Column(String, index=True)