from fastapi import FastAPI

app = FastAPI(
    title="PAMPS",
    description="PAMPS API - is posting app",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Hello World"}