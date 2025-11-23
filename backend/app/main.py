from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base
from app.api import auth, users

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI React Boilerplate")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "FastAPI React Boilerplate API"}


@app.get("/health")
def health():
    return {"status": "healthy"}
