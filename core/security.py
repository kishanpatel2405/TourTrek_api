import base64
import hashlib
import hmac
import json
from datetime import datetime, timedelta

from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

from utils.errors import TokenError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "qwertyuiop"


def hash_password(password: str) -> str:
    """Hash the password with bcrypt"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify the plain password against the hashed password"""
    return pwd_context.verify(plain_password, hashed_password)


def encode_jwt(data: dict, expires_delta: timedelta = timedelta(hours=1)) -> str:
    """Encode the data into JWT token"""
    header = {"alg": "HS256", "typ": "JWT"}

    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})

    to_encode["exp"] = to_encode["exp"].isoformat()

    encoded_header = (
        base64.urlsafe_b64encode(json.dumps(header).encode("utf-8"))
        .decode("utf-8")
        .rstrip("=")
    )
    encoded_payload = (
        base64.urlsafe_b64encode(json.dumps(to_encode).encode("utf-8"))
        .decode("utf-8")
        .rstrip("=")
    )

    signature = hmac_sha256(f"{encoded_header}.{encoded_payload}", SECRET_KEY)

    return f"{encoded_header}.{encoded_payload}.{signature}"


def hmac_sha256(message: str, secret: str) -> str:
    """Create HMAC-SHA256 signature"""
    key = secret.encode("utf-8")
    msg = message.encode("utf-8")
    signature = hmac.new(key, msg, hashlib.sha256).digest()
    return base64.urlsafe_b64encode(signature).decode("utf-8").rstrip("=")


def decode_jwt(jwt_token: str) -> dict:
    """Decode JWT token"""
    header_b64, payload_b64, signature_b64 = jwt_token.split(".")
    header = json.loads(base64.urlsafe_b64decode(header_b64 + "==").decode("utf-8"))
    payload = json.loads(base64.urlsafe_b64decode(payload_b64 + "==").decode("utf-8"))

    expected_signature = hmac_sha256(f"{header_b64}.{payload_b64}", SECRET_KEY)
    if expected_signature != signature_b64:
        raise Exception("Invalid token signature.")

    return payload


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            try:
                return self.verify_jwt(credentials.credentials)
            except TokenError as e:
                raise HTTPException(status_code=403, detail=str(e))
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwt_token: str): ...
