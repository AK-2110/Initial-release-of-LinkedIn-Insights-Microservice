from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models.page import Page
import os

async def init_db():
    # Check if we should use mock (e.g. if simpler for demo)
    # or just try to connect and fallback?
    # For this environment, let's default to Mongomock for stability if not in Docker.
    
    try:
        if "localhost" in settings.MONGO_URI and os.environ.get("USE_REAL_MONGO") != "true":
             # Fallback to mock for seamless demo experience if no local mongo
            from mongomock_motor import AsyncMongoMockClient
            client = AsyncMongoMockClient()
            print("Using In-Memory MongoDB (Mock) for Demo")
        else:
            client = AsyncIOMotorClient(settings.MONGO_URI)
            
        await init_beanie(database=client[settings.DB_NAME], document_models=[Page])
    except Exception as e:
        print(f"DB Init Error: {e}")
        # Final fallback
        from mongomock_motor import AsyncMongoMockClient
        client = AsyncMongoMockClient()
        await init_beanie(database=client[settings.DB_NAME], document_models=[Page])
