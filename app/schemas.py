from pydantic import BaseModel
from typing import List

class Interval(BaseModel):
    producer: str
    interval: int
    previousWin: int
    followingWin: int

class IntervalsResponse(BaseModel):
    min: List[Interval]
    max: List[Interval]