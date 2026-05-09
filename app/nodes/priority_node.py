class PriorityNode:
    def process(self, intent: str, message: str) -> str:
        """
        Detects priority or risk. 
        High priority for security issues, missing funds, lost cards.
        Medium priority for transaction failures.
        Low priority for general info.
        """
        high_priority_intents = [
            "lost_or_stolen_card",
            "direct_debit_payment_not_recognised",
            "wrong_amount_of_cash_received",
            "unable_to_verify_identity",
            "passcode_forgotten"
        ]
        
        medium_priority_intents = [
            "declined_cash_withdrawal",
            "declined_transfer",
            "failed_transfer",
            "card_not_working",
            "virtual_card_not_working",
            "card_payment_wrong_exchange_rate",
            "extra_charge_on_statement",
            "wrong_exchange_rate_for_cash_withdrawal",
            "pending_card_payment"
        ]

        if intent in high_priority_intents:
            return "High"
        elif intent in medium_priority_intents:
            return "Medium"
        elif "urgent" in message.lower() or "help" in message.lower() or "fraud" in message.lower():
            return "High"
        else:
            return "Low"
