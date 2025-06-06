from fastapi import APIRouter

router = APIRouter()


@router.post("/signup")
async def signup():
    return {"message": "User signed up successfully"}


@router.post("/login")
async def login():
    return {"message": "User logged in successfully"}


@router.post("/logout")
async def logout():
    return {"message": "User logged out successfully"}
