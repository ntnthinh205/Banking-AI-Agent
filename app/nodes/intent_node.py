class IntentNode:
    def __init__(self):
        # TODO: Load the fine-tuned model from Lab 2 here
        # e.g., self.model = load_model(settings.INTENT_MODEL_PATH)
        
        # Mapping keywords to intents. 
        # More specific/multi-word conditions are placed first to ensure correct matching.
        self.intent_rules = {
            "exchange rate payment": "card_payment_wrong_exchange_rate",
            "exchange rate withdrew cash": "wrong_exchange_rate_for_cash_withdrawal",
            "exchange rate": "exchange_rate",
            "wrong amount atm": "wrong_amount_of_cash_received",
            "unable verify": "unable_to_verify_identity",
            "documents verify": "verify_my_identity",
            "verification code top": "verify_top_up",
            "why verify": "why_verify_identity",
            "card not working": "card_not_working",
            "virtual not working": "virtual_card_not_working",
            "failed transfer": "failed_transfer",
            "transfer declined": "declined_transfer",
            "cash declined": "declined_cash_withdrawal",
            "top up debit card": "topping_up_by_card",
            "automatic top": "automatic_top_up",
            "atm support": "atm_support",
            "apple pay": "card_linking",
            "direct debit": "direct_debit_payment_not_recognised",
            "exchange fee": "exchange_charge",
            "extra charge": "extra_charge_on_statement",
            "forgot passcode": "passcode_forgotten",
            "activate": "activate_my_card",
            "age": "age_limit",
            "old": "age_limit",
            "arrive": "card_arrival",
            "arrival": "card_arrival",
            "delivery": "card_delivery_estimate",
            "link": "card_linking",
            "rejected": "card_not_working",
            "weekend": "exchange_charge",
            "disposable": "get_disposable_virtual_card",
            "physical": "get_physical_card",
            "lost": "lost_or_stolen_card",
            "stolen": "lost_or_stolen_card",
            "pending": "pending_card_payment",
            "currencies": "supported_cards_and_currencies"
        }

    def process(self, message: str) -> str:
        """
        Detects the intent of the message.
        Placeholder logic mapping keywords to labels via dictionary rules.
        Replace this entirely with your model inference once ready.
        """
        message = message.lower()
        
        for keywords, label in self.intent_rules.items():
            # Check if all keywords for this rule are present in the message
            if all(word in message for word in keywords.split()):
                return label
                
        return "default"
