from typing import List, Optional
from beanie import Document
from pydantic import BaseModel, Field
from datetime import datetime

class Comment(BaseModel):
    user_name: str
    text: str
    published_at: Optional[datetime] = None

class Post(BaseModel):
    id: str  # LinkedIn post URN or ID
    content: str
    likes_count: int = 0
    comments_count: int = 0
    published_at: Optional[datetime] = None
    comments: List[Comment] = []

class SocialMediaUser(BaseModel):
    name: str
    profile_url: Optional[str] = None
    designation: Optional[str] = None

class Page(Document):
    # VALIDATION NOTE:
    # 'page_id' allows both semantic slugs (e.g. 'openai') and numeric IDs.
    # Enforced uniqueness at the DB level to prevent duplicate scraping jobs.
    page_id: str = Field(..., unique=True)
    linkedin_internal_id: Optional[str] = None
    name: str
    url: str
    profile_pic_url: Optional[str] = None
    description: Optional[str] = None
    website: Optional[str] = None
    industry: Optional[str] = None
    followers_count: int = 0
    head_count: Optional[int] = None
    specialties: List[str] = []
    ai_summary: Optional[str] = None
    
    # Embedded lists (since requirements specify retaining only top few posts)
    posts: List[Post] = []
    employees: List[SocialMediaUser] = []
    
    last_scraped_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "pages"
