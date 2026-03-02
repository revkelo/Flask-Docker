from fastapi import FastAPI

app = FastAPI(title="FastAPI on Docker")


@app.get("/")
def root():
    return {"ok": True, "message": "Hello from FastAPI"}


@app.get("/health")
def health():
    return {"status": "healthy"}

