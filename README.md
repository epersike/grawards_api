# Grawards API

Grawards API is a FastAPI-based application that provides endpoints to retrieve movie data and calculate intervals between wins for producers.

## Features

- Retrieve movie data from the database
- Calculate minimum and maximum intervals between wins for producers
- Automatically initialize the database from a CSV file

## Requirements

- Python 3.8+
- Docker (for containerized development and deployment)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/grawards.git
cd grawards/backend
```

2. Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

pip install -r requirements.dev.txt

4. Create a .env file in the app directory with the following content:

```sh
DATABASE_URL=sqlite:///./db/movies.db
```

# Running the Application
## Using Docker
1. Build and run the Docker container:

```sh
docker compose -f docker-compose.dev.yml up --build
```

2. The API will be available at http://localhost:8000

### Makefile Commands

The Makefile provides several commands to manage the application using Docker:

- make build: Build the Docker image.
- make run: Run the Docker container in detached mode.
- make logs: View the logs of the running container.
- make stop: Stop the running container.
- make rm: Remove the stopped container.
- make exec: Open a bash shell inside the running container.
- make reset: Stop, remove, build, and run the container.
- make test: Run the tests inside the Docker container.

## Using Uvicorn

1. Run the application with Uvicorn:

```sh
uvicorn app.main:app --reload
```

2. The API will be available at http://localhost:8000.

## Endpoints

- GET / - Root endpoint to check if the API is online and its version
- GET /intervals - Get the minimum and maximum intervals between wins for producers

## Running Tests

1. Run the tests:
```sh
pytest
```

## Project Structure
```sh
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── db.py
│   ├── controllers.py
│   ├── schemas.py
│   └── tests/
│       └── test_main.py
├── db/
│   └── movielist.csv
├── docker-compose.dev.yml
├── Dockerfile.dev
├── requirements.txt
└── .env
```

# License
This project is licensed under the MIT License. See the LICENSE file for details.