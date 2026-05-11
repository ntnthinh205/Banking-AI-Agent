from app.clients.ollama_client import OllamaClient

class DraftNode:
    def __init__(self):
        self.llm_client = OllamaClient()

    def process(self, message: str, intent: str, priority: str, policy: str) -> str:
        """
        Generates a draft response using Ollama LLM.
        """
        system_prompt = "You are a polite, concise, and professional banking customer support agent. Do not make up facts."
        
        prompt = f"""
Customer message: "{message}"
Detected Intent: {intent}
Priority Level: {priority}
Relevant Policy: "{policy}"

Draft a response to the customer based primarily on the Relevant Policy.
"""
        draft = self.llm_client.generate_response(prompt, system=system_prompt)
        
        if not draft:
            draft = "I apologize, but I am unable to generate a detailed response right now. Please wait or contact a human agent."
            
        return draft.strip()
