# Mini URL Shortener

A simple URL shortener built with FastAPI.

## Endpoints

- **POST /shorten**: Shorten a URL
  - Body: `{"url": "https://example.com"}`
  - Response: `{"short_code": "abc123"}`

- **GET /{code}**: Redirect to the original URL
  - Redirects to the stored URL

- **GET /stats**: Get statistics
  - Response: `{"total_urls": 1, "urls": {"abc123": "https://example.com"}}`

## Running

1. Install dependencies: `pip install -r requirements.txt`
2. Run: `uvicorn main:app --reload`

The server will run on http://localhost:8000

## API Documentation

Visit http://localhost:8000/docs for interactive API docs.