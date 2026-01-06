# Veefyed Image Analysis API (Mock Backend Task)

A small, backend-focused FastAPI service built as part of a technical task.
The service allows a mobile client to upload an image, perform a mock image analysis, and receive structured JSON results.

This project demonstrates:

- Backend API design
- Image upload handling and validation
- Clean code structure
- End-to-end mobile → backend → response flow

**Note:** This project intentionally does not use real AI/ML. All analysis logic is simulated.

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **API Type:** REST
- **Storage:** Local filesystem

## Running the Service Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at:
http://localhost:8000

## Optional API Key Authentication

You may optionally protect the API using a simple API key:

```bash
export API_KEY="your-secret-key"
```

When enabled, all requests must include:
```
x-api-key: your-secret-key
```

## API Endpoints

### 1. Upload Image

**POST /upload**

Uploads an image for later analysis.

- **Content-Type:** multipart/form-data
- **Form field:** file
- **Allowed formats:** JPEG, PNG
- **Max file size:** 5MB

**Example request:**

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "x-api-key: your-secret-key" \
  -F "file=@/path/to/image.jpg"
```

**Example response:**

```json
{
  "image_id": "abc123"
}
```

### 2. Analyze Image

**POST /analyze**

Performs mock analysis on a previously uploaded image.

- **Content-Type:** application/json

**Example request:**

```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-secret-key" \
  -d '{"image_id": "abc123"}'
```

**Example response:**

```json
{
  "image_id": "abc123",
  "skin_type": "Oily",
  "issues": ["Hyperpigmentation"],
  "confidence": 0.87
}
```

## Error Handling

The API returns meaningful HTTP status codes and error messages:

### 400 Bad Request
- Invalid file type
- File size exceeds 5MB
- Missing or empty image_id

### 404 Not Found
- Image not found for the given image_id

FastAPI validation errors (422) are returned automatically where applicable.

## Project Structure

```
app/
  main.py
  routes/
    upload.py
    analyze.py
  services/
    storage_service.py
    analysis_service.py
  utils/
    validators.py
  models/
    schemas.py
uploads/
README.md
requirements.txt
```

The structure separates routing, business logic, validation, and schemas to keep the codebase readable and maintainable.

## Assumptions

- Images are stored locally in the uploads/ directory.
- No database is used; the filesystem acts as temporary storage.
- Analysis logic is fully mocked and deterministic.
- Authentication is optional and intentionally simple.

## What I Would Improve for Production

If this were production-ready, the next steps would include:

- Persist image metadata in a database (e.g. PostgreSQL)
- Move image storage to object storage (e.g. S3)
- Add per-user authentication and authorization
- Run analysis asynchronously using background workers
- Add rate limiting and request throttling
- Perform deeper image validation and virus scanning
- Add structured logging, metrics, and tracing
- Add automated tests and CI pipeline

## Optional Docker Support

To run the service in Docker:

```bash
docker build -t image-analysis-api .
docker run -p 8000:8000 image-analysis-api
```
