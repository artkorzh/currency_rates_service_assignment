from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import make_async_session


async def get_db() -> AsyncSession:
    """
    Dependency function that yields db sessions
    """
    async with make_async_session() as session:
        yield session
        await session.commit()
