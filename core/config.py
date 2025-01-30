import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Find Your Tour API"
    API_VERSION: str = "1.0.0"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "defaultsecretkey")

settings = Settings()
