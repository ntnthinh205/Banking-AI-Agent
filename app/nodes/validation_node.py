class ValidationNode:
    def process(self, draft: str, policy: str) -> bool:
        """
        Validates the generated draft.
        Returns True if the draft is acceptable, False otherwise.
        """
        if len(draft) < 10:
            return False
            
        # A simple check: if the draft doesn't contain at least one word from the policy (excluding common stop words)
        # This is a very basic validation logic.
        policy_words = set(policy.lower().split())
        draft_words = set(draft.lower().split())
        
        # Check intersection
        intersection = policy_words.intersection(draft_words)
        
        # We assume if they have at least 3 words in common it's loosely following the policy
        if len(intersection) < 3 and "unable" not in draft.lower():
             return False

        return True
