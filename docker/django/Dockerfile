FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
    # psycopg2 dependencies
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    # Pillow dependencies
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    # CFFI dependencies
    && apk add libffi-dev py-cffi

COPY ./docker/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Celery config
COPY ./docker/django/celery/start-worker /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

RUN mkdir app
WORKDIR /app
COPY . /app