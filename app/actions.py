from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.tables.symbols import Symbol
from app.models.schema.symbols import InSymbolSchema


async def create_symbol(session: AsyncSession, in_symbol: InSymbolSchema) -> Symbol:
    orm_symbol = Symbol(**in_symbol.dict())
    session.add(orm_symbol)
    await session.flush()
    return orm_symbol


async def get_symbols(session: AsyncSession) -> list[Symbol]:
    result = await session.execute(select(Symbol))
    return result.scalars().all()
