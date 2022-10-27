import asyncio
from unittest import mock

import pytest
from hamcrest import assert_that, contains_inanyorder
from httpx import AsyncClient
from starlette import status

pytestmark = pytest.mark.asyncio


async def test_create(async_client: AsyncClient) -> None:
    response = await async_client.post("/v1/symbols/", json={"symbol": "EURUSD"})

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "symbol": "EURUSD",
        "id": mock.ANY,
    }


async def test_get_symbols(async_client: AsyncClient) -> None:
    await async_client.post("/v1/symbols/", json={"symbol": "EURUSD"})
    await async_client.post("/v1/symbols/", json={"symbol": "USDJPY"})

    response = await async_client.get("/v1/symbols/")
    assert response.status_code == status.HTTP_200_OK

    assert_that(
        response.json(),
        contains_inanyorder(
            {"symbol": "EURUSD", "id": mock.ANY},
            {"symbol": "USDJPY", "id": mock.ANY},
        ),
    )
