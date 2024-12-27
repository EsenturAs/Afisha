FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/reqirements.txt

RUN pip install -r /app/requirements.txt
COPY . .
