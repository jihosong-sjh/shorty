from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str | None = None

settings = Settings()
