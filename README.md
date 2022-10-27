# SQLAlchemy ORM 1.4 with FastAPI on asyncio

This project is originally based on [this repository](https://github.com/rglsk/fastapi-sqlalchemy-1.4-async).

## Run project
`docker-compose up -d app`

## Run db
`docker-compose up -d postgres`

## Run tests
`docker compose run --rm tests`

## Generate migrations
`docker-compose run app alembic revision --autogenerate`

## Run migrations
`docker-compose run app alembic upgrade head`

## Format code
`poetry run black .`
