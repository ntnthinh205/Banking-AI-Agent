# Dummy policy database to simulate retrieval based on 30 specific intents

POLICIES = {
    "activate_my_card": "To activate your card, log in to the mobile app and navigate to 'Cards', then select 'Activate'. You will need the CVV on the back of the card.",
    "age_limit": "To open an account, you must be at least 18 years old. Minors aged 13-17 can open a restricted account with a parent or guardian's consent.",
    "atm_support": "You can use your card at any ATM that supports Visa or Mastercard. Please note that third-party ATM operators may charge a fee.",
    "automatic_top_up": "Automatic top-up can be configured in the app under 'Settings' > 'Top-ups'. You can set a minimum balance and a top-up amount.",
    "card_arrival": "Cards typically arrive within 5-7 business days. If you haven't received it after 10 days, please request a replacement in the app.",
    "card_delivery_estimate": "Standard delivery takes 5-7 business days, while express delivery takes 2-3 business days. You can track the delivery status in the app.",
    "card_linking": "You can link your card to Apple Pay or Google Pay directly from our mobile app under the 'Cards' tab by selecting 'Add to Wallet'.",
    "card_not_working": "If your card is not working, check if it's frozen in the app, ensure you haven't exceeded your daily limits, or verify that the PIN is correct.",
    "card_payment_wrong_exchange_rate": "We use the real-time interbank exchange rate. Sometimes merchants may apply their own dynamic currency conversion rate, which we cannot control.",
    "declined_cash_withdrawal": "Cash withdrawals may be declined due to insufficient funds, exceeding daily ATM limits, or suspicious activity. Check your app for specific decline reasons.",
    "declined_transfer": "Transfers can be declined if details are incorrect, limits are exceeded, or for security reasons. Please verify the recipient details and try again.",
    "direct_debit_payment_not_recognised": "If you don't recognize a direct debit, please check your subscriptions. If it's fraudulent, you can block it in the app and report it to us.",
    "exchange_charge": "We do not charge extra exchange fees on weekdays. However, a small markup (usually 0.5-1%) may apply on weekends.",
    "exchange_rate": "You can check the current exchange rates at any time in the app. Rates are updated in real-time.",
    "extra_charge_on_statement": "Extra charges might be due to merchant pre-authorizations (which will drop off), subscription renewals, or currency exchange fees.",
    "failed_transfer": "If a transfer fails, the funds will typically bounce back to your account within 1-3 business days. Double-check the recipient's details.",
    "get_disposable_virtual_card": "You can generate a disposable virtual card in the app under 'Cards' > 'Virtual'. Its details will change after each transaction for security.",
    "get_physical_card": "You can order a physical card from the 'Cards' tab in the app. The first card is free, and replacements may incur a small fee.",
    "lost_or_stolen_card": "If your card is lost or stolen, freeze it immediately in the app under 'Cards' > 'Freeze'. Then, you can order a replacement card.",
    "passcode_forgotten": "If you've forgotten your app passcode, select 'Forgot Passcode' on the login screen. You will need to verify your identity with your email and ID.",
    "pending_card_payment": "Pending payments are pre-authorizations by the merchant. They usually settle or drop off within 7-10 days. We cannot manually cancel them.",
    "supported_cards_and_currencies": "We support over 30 major currencies. You can hold and exchange them directly in the app. We accept Visa and Mastercard for top-ups.",
    "topping_up_by_card": "You can top up your account instantly using another debit or credit card. Make sure the billing address matches your account details.",
    "unable_to_verify_identity": "If automatic verification fails, make sure your ID is clear and well-lit. If it still fails, you may need to submit documents for manual review.",
    "verify_my_identity": "Identity verification requires a valid government-issued ID (passport or driver's license) and a quick selfie video in the app.",
    "verify_top_up": "For security, some top-ups require 3D Secure verification. Please follow the prompt sent to your banking app or SMS to authorize it.",
    "virtual_card_not_working": "If your virtual card is failing, ensure you have sufficient balance and the card is not frozen. Some merchants do not accept virtual cards.",
    "why_verify_identity": "We are legally required to verify your identity to comply with anti-money laundering (AML) and know-your-customer (KYC) regulations.",
    "wrong_amount_of_cash_received": "If an ATM gave you the wrong amount, the ATM operator usually rectifies this within 7 days. If not, please file a dispute with us.",
    "wrong_exchange_rate_for_cash_withdrawal": "When withdrawing cash abroad, always choose to be charged in the local currency to avoid the ATM operator's poor exchange rates.",
    "default": "Please refer to the general FAQ on our website or speak with a representative for more details."
}

def get_policy(intent: str) -> str:
    """Retrieve policy based on intent."""
    return POLICIES.get(intent, POLICIES["default"])
