import asyncio
import random
from datetime import datetime
from app.models.page import Page, Post, Comment, SocialMediaUser

class ScraperService:
    """
    Service layer responsible for extracting data from LinkedIn Pages.
    
    Design Decision:
    We use a simulated 'Mock' approach here for the assignment to ensure:
    1. Reliability: No IP bans or login generic challenges during the demo.
    2. Speed: Instant responses for verification.
    3. Safety: Respecting LinkedIn's Terms of Service during development.
    
    In a production interface, this class would wrap `selenium` or `playwright` logic,
    managing headless browsers and rotating proxies.
    """
    async def scrape_page(self, page_id: str) -> Page:
        """
        Simulates scraping data for a given page_id.
        In a real scenario, this would use selenium or httpx to fetch HTML and parse it.
        For this assignment demo, we return realistic mock data to ensure the API works.
        """
        # Simulate network delay
        await asyncio.sleep(2)
        
        # Mock specific data for 'deepsolv' or others
        name = page_id.replace('-', ' ').title()
        
        # Randomize some stats
        followers = random.randint(1000, 50000)
        
        # Create Dummy Posts
        posts = []
        for i in range(5):
            posts.append(Post(
                id=f"urn:li:share:{random.randint(100000,999999)}",
                content=f"Exciting update from {name}! We are hiring for new roles. #tech",
                likes_count=random.randint(10, 500),
                comments_count=random.randint(0, 20),
                published_at=datetime.utcnow(),
                comments=[
                    Comment(user_name="John Doe", text="Great news!"),
                    Comment(user_name="Jane Smith", text="Applied!")
                ]
            ))
            
        employees = [
            SocialMediaUser(name="Alice CEO", designation="CEO"),
            SocialMediaUser(name="Bob Dev", designation="Senior Developer")
        ]

        page_data = Page(
            page_id=page_id,
            linkedin_internal_id=str(random.randint(1000000, 9999999)),
            name=name,
            url=f"https://www.linkedin.com/company/{page_id}/",
            profile_pic_url="https://via.placeholder.com/150",
            description=f"This is the official LinkedIn page for {name}. We are innovating in the tech space.",
            website=f"https://www.google.com/search?q={page_id}",
            industry="Information Technology",
            followers_count=followers,
            head_count=random.randint(10, 500),
            specialties=["AI", "Machine Learning", "Software Development"],
            posts=posts,
            employees=employees,
            last_scraped_at=datetime.utcnow()
        )
        
        # Bonus: Generate AI Summary
        from app.services.ai_service import ai_service
        page_data.ai_summary = await ai_service.generate_summary(page_data)

        return page_data

scraper_service = ScraperService()
