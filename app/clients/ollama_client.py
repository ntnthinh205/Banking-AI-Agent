import requests
from app.clients.base import BaseClient
from app.core.settings import settings

class OllamaClient(BaseClient):
    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL
        self.model = settings.LLM_MODEL

    def generate_response(self, prompt: str, system: str = None) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        if system:
            payload["system"] = system

        try:
            # Tăng timeout lên 120s vì đôi khi mô hình chạy trên CPU sẽ hơi chậm
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")
        except requests.exceptions.RequestException as e:
            print(f"Error calling Ollama: {e}")
            return ""
