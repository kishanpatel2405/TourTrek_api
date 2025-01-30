from fastapi import FastAPI
from api.v1.router import router as api_router
from core.events import add_event_handlers

app = FastAPI()

add_event_handlers(app)

app.include_router(api_router, prefix="/api/v1")
