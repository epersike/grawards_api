FROM python:3.11.11-slim

WORKDIR /app

COPY app/ .
COPY db/ ./db

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]