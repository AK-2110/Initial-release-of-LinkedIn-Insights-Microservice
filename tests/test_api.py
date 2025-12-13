import pytest
from httpx import AsyncClient
from app.main import app
from app.models.page import Page

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to LinkedIn Insights Service. Visit /docs for API documentation."}

@pytest.fixture(autouse=True)
async def init_test_db():
    from app.core.database import init_db
    await init_db()

@pytest.mark.asyncio
async def test_get_insight_mock():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/insight/test-company")
    assert response.status_code == 200
    data = response.json()
    assert data["page_id"] == "test-company"
    assert "Mock Mode" in data.get("ai_summary", "")

@pytest.mark.asyncio
async def test_search():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create a page first using the get endpoint
        await ac.get("/api/v1/insight/searchable-company")
        
        response = await ac.get("/api/v1/insights/search?name=searchable")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["page_id"] == "searchable-company"
