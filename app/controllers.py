import re
from sqlalchemy.orm import Session
from collections import defaultdict
from typing import List, Dict
from app.models import Movie
from app.db import SessionLocal

def read_movies_from_db() -> List[Movie]:
    '''
        Read all movies from the database and return them as a list of 
        Movie models.
    '''
    db: Session = SessionLocal()
    movies = db.query(Movie).all()
    db.close()

    return movies

def calculate_intervals(data: List[Movie]) -> Dict[str, List[Dict[str, int]]]:
    '''
        Calculate the minimum and maximum intervals between wins for producers.
    '''
    producer_wins = defaultdict(list)

    # Let's create a dictionary with the producers as keys and a list of years he won.
    for row in data:
        if row.winner.strip().lower() == 'yes':
            # Movies may have more than one producer separeted by commas 
            # or the word "and"...
            # so we split producers on commas and the word "and"
            producers = re.split(r',\s*|\s*and\s*', row.producers)
            for producer in producers:
                producer_wins[producer.strip()].append(int(row.year))

    # Now we calculate the intervals between wins for each producer
    intervals = []
    for producer, years in producer_wins.items():
        years.sort()
        for i in range(1, len(years)):
            intervals.append({
                'producer': producer,
                'interval': years[i] - years[i - 1],
                'previousWin': years[i - 1],
                'followingWin': years[i]
            })

    if not intervals:
        return {'min': [], 'max': []}

    min_interval = min(intervals, key=lambda x: x['interval'])['interval']
    max_interval = max(intervals, key=lambda x: x['interval'])['interval']

    min_intervals = [interval for interval in intervals if interval['interval'] == min_interval]
    max_intervals = [interval for interval in intervals if interval['interval'] == max_interval]

    return {'min': min_intervals, 'max': max_intervals}