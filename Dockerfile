# syntax = docker/dockerfile:1

FROM python:3.9.13-slim-buster

WORKDIR /app

COPY . .

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV NAME World

CMD ["python","./app.py"]



