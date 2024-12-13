import pytest
from fastapi.testclient import TestClient
from ..main import app
from ..db import initialize_database, SessionLocal
from ..models import Movie

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Initializes the database and inserts test data
    initialize_database()
    db = SessionLocal()
    db.query(Movie).delete()
    db.commit()
    db.close()

    yield

    # Cleans up the database after tests
    db = SessionLocal()
    db.query(Movie).delete()
    db.commit()
    db.close()

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "version" in response.json()"

def test_intervals():
    response = client.get("/intervals")
    assert response.status_code == 200
    data = response.json()
    assert "min" in data
    assert "max" in data
    assert isinstance(data["min"], list)
    assert isinstance(data["max"], list)

def test_initialize_database():
    initialize_database()
    db = SessionLocal()
    movies = db.query(Movie).all()
    db.close()
    assert len(movies) > 0