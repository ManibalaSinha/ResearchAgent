from pydantic_settings import BaseSettings
print(BaseSettings)
from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env manually
env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env"
load_dotenv(env_path)

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False
    BACKOFF: list[int] = [1, 2, 4]  # default retry delays

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # if BACKOFF comes as string from env, convert to list[int]
        if isinstance(self.BACKOFF, str):
            self.BACKOFF = [int(x) for x in self.BACKOFF.split(",")]

# instantiate settings
settings = Settings()