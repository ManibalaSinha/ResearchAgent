import pytest

from app.tools.document_search import document_search


@pytest.mark.asyncio
async def test_document_search_success():
    result = await document_search("FastAPI")

    assert len(result) == 2
    assert "FastAPI is a Python framework for building APIs." in result
    assert "FastAPI supports asynchronous endpoints." in result


@pytest.mark.asyncio
async def test_document_search_no_results():
    result = await document_search("Django")

    assert result == []


@pytest.mark.asyncio
async def test_document_search_case_insensitive():
    result = await document_search("FASTAPI")

    assert len(result) == 2


@pytest.mark.asyncio
async def test_document_search_partial_match():
    result = await document_search("PostgreSQL")

    assert result == [
        "PostgreSQL is a relational database."
    ]


@pytest.mark.asyncio
async def test_document_search_empty_query():
    result = await document_search("")

    assert result == []
