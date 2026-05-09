from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Set this to your local or Pinggy Ollama URL
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    LLM_MODEL: str = "gpt-oss-20b"  # Replace with the actual model you are using
    INTENT_MODEL_PATH: str = "./models/intent_model" # Path to your Lab 2 model

    class Config:
        env_file = ".env"

settings = Settings()
