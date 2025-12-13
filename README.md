# LinkedIn Insights Microservice

A FastAPI-based microservice to scrape, store, and analyzing LinkedIn Page insights.

## Features
- **Scraping**: Fetches page details, posts, and employees (Simulated for stability).
- **Storage**: MongoDB with Beanie ODM.
- **Search**: Filter pages by name, industry, and follower counts.
- **AI Summary**: (Bonus) Generates a summary of the page using AI (Mock/OpenAI).
- **Dockerized**: specific `docker-compose` setup.

## Setup & Run

### Prerequisites
- Docker & Docker Compose
- (Optional) Python 3.11+ for local run

### Running with Docker (Recommended)
```bash
docker-compose up --build
```
The API will be available at `http://localhost:8000`.
Docs: `http://localhost:8000/docs`

### Running Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure MongoDB is running locally at `mongodb://localhost:27017`.
3. Run server:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints
- `GET /api/v1/insight/{page_id}`: Get or scrape page details.
- `GET /api/v1/insights/search`: Search pages with filters.

## Project Structure
- `app/models`: Database schemas.
- `app/routers`: API route handlers.
- `app/services`: Business logic (Scraper, AI).
- `app/core`: Config and DB setup.
