from fastapi import APIRouter
from schemas.v1.items import Item

router = APIRouter()

@router.get("/{item_id}")
def get_item(item_id: int):
    # Logic to get item by ID (no DB yet)
    return {"item_id": item_id, "name": "Sample Item"}
