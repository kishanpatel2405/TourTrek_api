from fastapi import APIRouter
from .endpoints import users, auth, items

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(items.router, prefix="/items", tags=["items"])
