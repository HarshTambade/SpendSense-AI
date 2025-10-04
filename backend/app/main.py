from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, users, expenses, approvals, analytics

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SpendSense AI",
    description="Smart Expense Management Platform with AI",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(expenses.router)
app.include_router(approvals.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to SpendSense AI",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
