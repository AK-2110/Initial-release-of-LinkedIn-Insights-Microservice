import os
from app.models.page import Page
from app.core.config import settings
import httpx

class AIService:
    async def generate_summary(self, page: Page) -> str:
        """
        Generates a summary using an LLM.
        """
        if settings.OPENAI_API_KEY:
            # Real simplified OpenAI call logic
            try:
                prompt = (
                    f"Summarize the LinkedIn page for {page.name}. "
                    f"They are in {page.industry} with {page.followers_count} followers. "
                    f"Description: {page.description}. "
                    f"Top posts content: {[p.content for p in page.posts[:3]]}."
                )
                
                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        "https://api.openai.com/v1/chat/completions",
                        headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                        json={
                            "model": "gpt-3.5-turbo",
                            "messages": [{"role": "user", "content": prompt}]
                        },
                        timeout=10.0
                    )
                    if response.status_code == 200:
                        data = response.json()
                        return data["choices"][0]["message"]["content"]
            except Exception as e:
                print(f"AI Service Error: {e}")
                # Fallback to mock
        
        # Mock Response
        return (
            f"AI Summary for {page.name}: This company operates in the {page.industry} sector "
            f"and has a strong following of {page.followers_count}. "
            f"Note: This is a generated summary (Mock Mode)."
        )

ai_service = AIService()
