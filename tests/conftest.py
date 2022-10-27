import pytest
from fastapi import FastAPI

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import Base
from app.db.session import make_async_session, engine


@pytest.fixture(name="db_session")
async def db_session_fixture() -> AsyncSession:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
        async with make_async_session(bind=connection) as session:
            yield session
            await session.flush()
            await session.rollback()

    # Prevent SQLAlchemy concurrency issues.
    # It seems like connection pool preserves a pointer to an old event pool.
    await engine.dispose()


@pytest.fixture(name="app")
def app_fixture(db_session: AsyncSession) -> FastAPI:
    from app.api.dependencies.db import get_db
    from app.main import app

    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    return app


@pytest.fixture()
async def async_client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
