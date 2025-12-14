# LinkedIn Insights Microservice

A FastAPI-based microservice to scrape, store, and analyzing LinkedIn Page insights.

## 🚀 Features

- **Premium Web Dashboard**: Interactive Glassmorphism UI for real-time insights (Vue.js + Tailwind).
- **AI-Powered Summaries**: Generates executive summaries of company profiles.
- **Robust Scraper**: (Mocked for stability) Fetches posts, employees, and follower stats.
- **RESTful API**: Fully documented FastAPI endpoints.
- **MongoDB Storage**: Scalable document storage with Beanie ODM.

## 🖥️ Usage

### 🌐 Online Demo (Live)
**[Click Here to Open Premium Dashboard](https://trek-author-succeed-idol.trycloudflare.com)**
*(Powered by Cloudflare Tunnel)*

### Web Dashboard (Local)
1.  Open [http://localhost:8000/](http://localhost:8000/) in your browser.
2.  Enter a Company Name (e.g., `openai`) or LinkedIn URL.
3.  Click **Analyze** to see real-time data.

### API Documentation
Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the Swagger UI.

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
