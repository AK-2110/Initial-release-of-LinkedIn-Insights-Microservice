from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import init_db
from app.routers import insights

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown (if needed)

app = FastAPI(
    title="LinkedIn Insights Microservice",
    description="API to scrape and store LinkedIn Page insights.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(insights.router, prefix="/api/v1", tags=["Insights"])

@app.get("/")
async def root():
    return {"message": "Welcome to LinkedIn Insights Service. Visit /docs for API documentation."}
