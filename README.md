# FastAPI + Docker (Render-ready)

## Run locally (Docker)

```bash
docker build -t fastapi-api .
docker run --rm -p 8000:8000 fastapi-api
```

- Docs: `http://localhost:8000/docs`
- OpenAPI: `http://localhost:8000/openapi.json`

## Deploy on Render

Create a **Web Service** and choose **Docker**; Render will build from `Dockerfile`.

- Render sets `PORT` automatically; this image listens on `$PORT` (fallback `8000`).

