from fastapi import APIRouter
from schemas.v1.users import User, UserCreate

router = APIRouter()

@router.post("/create")
def create_user(user: UserCreate):
    # Logic to create user (without DB for now)
    return {"msg": "User created", "user": user}

@router.get("/{user_id}")
def get_user(user_id: int):
    # Logic to get user by ID (without DB for now)
    return {"user_id": user_id, "name": "John Doe"}
