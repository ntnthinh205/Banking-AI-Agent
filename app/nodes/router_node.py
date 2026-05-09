class RouterNode:
    def process(self, priority: str, is_valid: bool) -> str:
        """
        Decides the final routing.
        """
        if priority == "High":
            return "escalate_to_human"
        elif not is_valid:
            return "ask_for_more_info_or_re_draft"
        else:
            return "reply_directly"
