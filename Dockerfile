FROM python:3.10.7-bullseye as base

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get -y update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip \
   && pip install poetry==1.2.2 \
   && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --only main

COPY ./app ./
ENV LOG_LEVEL info
ENV PYTHONPATH=.
CMD ["uvicorn", "app.main:app"]

# For development build
FROM base as dev

RUN poetry install --no-root
