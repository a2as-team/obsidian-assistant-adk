from google.adk.models.google_llm import Gemini
from google.genai import types
from .config import load_settings

settings = load_settings()

# Configure standard models for use within ADK
model_flash_lite = Gemini(model="gemini-2.5-flash-lite")
model_flash = Gemini(model="gemini-2.5-flash")
model_pro = Gemini(model="gemini-2.5-pro")

# Define retry configuration for Gemini models
retry_config = types.HttpRetryOptions(
    attempts=settings.http_retry_attempts,
    exp_base=settings.http_retry_exp_base,
    initial_delay=settings.http_retry_initial_delay,
    http_status_codes=settings.http_retry_codes,
)

# Apply retry configuration to each model
for model in [model_flash_lite, model_flash, model_pro]:
    model.retry_options = retry_config