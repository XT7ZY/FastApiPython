FROM python:3.9.2

LABEL maintainer="xtzzy@bk.ru"

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./src /code/src
COPY ./alembic.ini /code/alembic.ini
COPY ./migrations /code/migrations

RUN pip install --no-cache-dir --upgrade -r requirements.txt

