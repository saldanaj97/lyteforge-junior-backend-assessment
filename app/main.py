from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes import auth, items

app = FastAPI()

origins = [
    "*",  # Allow all origins for this assessment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

app.mount("/", StaticFiles(directory="static", html=True), name="static")
