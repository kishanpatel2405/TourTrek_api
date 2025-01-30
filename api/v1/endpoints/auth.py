from fastapi import APIRouter, Depends
from core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    # Logic to verify credentials (no DB yet)
    if verify_password(password, "hashed_password"):
        return {"access_token": create_access_token(username)}
    return {"msg": "Invalid credentials"}, 401
