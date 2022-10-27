from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.symbols import OutSymbolSchema, InSymbolSchema
from app import actions

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutSymbolSchema)
async def create_symbol(
    payload: InSymbolSchema, db_session: AsyncSession = Depends(get_db)
) -> Any:
    return await actions.create_symbol(db_session, payload)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[OutSymbolSchema])
async def get_symbols(db_session: AsyncSession = Depends(get_db)) -> Any:
    return await actions.get_symbols(db_session)
