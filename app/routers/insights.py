from fastapi import APIRouter, HTTPException, Query, Path
from typing import List, Optional
from app.models.page import Page
from app.services.scraper_service import scraper_service

router = APIRouter()

@router.get("/insight/{page_id:path}", response_model=Page)
async def get_page_insights(
    page_id: str = Path(..., description="The LinkedIn Page ID (e.g. deepsolv) or full URL")
):
    """
    Get insights for a specific LinkedIn Page ID or URL.
    Input can be 'deepsolv' or 'https://www.linkedin.com/company/deepsolv/'.
    """
    # ---------------------------------------------------------
    # INPUT NORMALIZATION LAYER
    # Handles both raw IDs and full URLs to provide a seamless UX.
    # ---------------------------------------------------------
    if "linkedin.com" in page_id:
        segments = [s for s in page_id.split("/") if s]
        if segments:
            page_id = segments[-1]
            
    # OPTIMIZATION NOTE:
    # In a high-traffic production env, checking Redis cache here 
    # would reduce MongoDB load by ~90% for frequently accessed pages.
    # Currently implemented with 'Write-Through' logic to DB.
    page = await Page.find_one({"page_id": page_id})
    
    if page:
        return page
    
    # If not found, scrape it
    try:
        scraped_page = await scraper_service.scrape_page(page_id)
        # Save to DB
        # Check collision again just in case (though highly unlikely in this simple flow)
        existing = await Page.find_one(Page.page_id == page_id)
        if not existing:
            await scraped_page.insert()
            return scraped_page
        return existing
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to scrape page: {str(e)}")

@router.get("/insights/search", response_model=List[Page])
async def search_pages(
    name: Optional[str] = Query(None, description="Search by partial page name"),
    industry: Optional[str] = Query(None, description="Filter by industry"),
    min_followers: Optional[int] = Query(None, description="Minimum followers count"),
    max_followers: Optional[int] = Query(None, description="Maximum followers count"),
    skip: int = 0,
    limit: int = 10
):
    """
    Search and filter pages in the database.
    """
    query = Page.find_all()
    
    if name:
        # Case insensitive regex search
        query = query.find({"name": {"$regex": name, "$options": "i"}})
    
    if industry:
        query = query.find({"industry": {"$regex": industry, "$options": "i"}})
        
    if min_followers is not None:
        query = query.find({"followers_count": {"$gte": min_followers}})
        
    if max_followers is not None:
        query = query.find({"followers_count": {"$lte": max_followers}})
        
    result = await query.skip(skip).limit(limit).to_list()
    return result
