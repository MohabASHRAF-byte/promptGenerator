import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import project_router

app = FastAPI()
from backend.config.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Allow all origins, all methods, and all headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# app.include_router(prompt_router)
app.include_router(project_router)


@app.get("/ping")
async def ping():
    return {"message": "pong !"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
