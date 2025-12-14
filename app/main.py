from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from app.core.database import init_db
from app.routers import insights

@asynccontextmanager
async def lifespan(app: FastAPI):
    # LIFESPAN EVENT HANDLER
    # ----------------------
    # We use a lifespan context manager here instead of the deprecated @app.on_event("startup")
    # to ensure the database connection is cleanly established before requests are accepted.
    # This matches modern FastAPI best practices (v0.100+).
    await init_db()
    yield
    # Shutdown logic (e.g., closing DB connections) would go here.

app = FastAPI(
    title="LinkedIn Insights Microservice",
    description="Enterprise-grade API for scraping and analyzing LinkedIn Page data. Architecture optimized for async IO.",
    version="1.0.0",
    lifespan=lifespan
)

# Mount Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(insights.router, prefix="/api/v1", tags=["Insights"])

@app.get("/")
async def read_root():
    return FileResponse('app/static/index.html')
