from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    
    google_api_key: str = Field(default="", validation_alias="GOOGLE_API_KEY")
    vault_path: Path = Field(default=BASE_DIR / "obsidian_vault", validation_alias="OBSIDIAN_VAULT_PATH")
    environment: str = Field(default="dev")

    # Retry settings for Gemini models
    http_retry_attempts: int = Field(default=3)
    http_retry_exp_base: int = Field(default=7)
    http_retry_initial_delay: int = Field(default=1)
    http_retry_codes: list[int] = Field(default=[429, 500, 503, 504])

def load_settings() -> Settings:
    return Settings()


