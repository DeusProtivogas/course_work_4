FROM python:3.8.5-slim

WORKDIR /code
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY data data
COPY game game
