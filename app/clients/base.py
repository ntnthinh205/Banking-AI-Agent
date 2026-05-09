from abc import ABC, abstractmethod

class BaseClient(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Generate response given a prompt."""
        pass
