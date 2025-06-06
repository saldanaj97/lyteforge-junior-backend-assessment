from fastapi import FastAPI

from app.api.routes import auth, items

app = FastAPI()

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
