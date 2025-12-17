from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE_MB: int
    FILE_DEFAULT_CHUNK_SIZE: int
    MONGODB_URI: str
    MONGODB_DATABASE: str

    # NEW: Use model_config with SettingsConfigDict
    model_config = SettingsConfigDict(
        env_file=".env",

        extra="ignore"  # Ignores extra fields in the .env file
    )

def get_settings():
    return Settings()