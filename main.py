from fastapi import FastAPI, Depends, HTTPException

from api.v1.router import router as api_router
from core.security import hash_password, verify_password, encode_jwt, JWTBearer

app = FastAPI()

fake_users_db = {}


@app.post("/register")
async def register(username: str, password: str):
    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already exists.")

    hashed_password = hash_password(password)
    fake_users_db[username] = {"password": hashed_password}
    return {"msg": "User registered successfully."}


@app.post("/login")
async def login(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials.")

    token = encode_jwt({"sub": username})
    return {"access_token": token}


# Protected endpoint (requires valid JWT token)
@app.get("/protected")
async def protected_route(payload: dict = Depends(JWTBearer())):
    return {"msg": "You have access", "user": payload["sub"]}


app.include_router(api_router, prefix="/api/v1")
