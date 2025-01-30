from fastapi import FastAPI
from starlette.events import Event

def add_event_handlers(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        print("Application is starting")

    @app.on_event("shutdown")
    async def shutdown_event():
        print("Application is shutting down")
