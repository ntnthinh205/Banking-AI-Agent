from app.data.policies import get_policy

class PolicyNode:
    def process(self, intent: str) -> str:
        """
        Retrieves the policy based on the intent.
        """
        return get_policy(intent)
