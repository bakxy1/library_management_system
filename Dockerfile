FROM python:alpine

WORKDIR /app

COPY requirements.txt /app/

RUN apk add --no-cache mariadb-dev gcc musl-dev python3-dev
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /app/