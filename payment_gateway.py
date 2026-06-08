"""
Payment Gateway — handles charging via different payment methods
"""
import logging
import uuid

logger = logging.getLogger(__name__)

SUPPORTED_METHODS = ["credit_card", "debit_card", "paypal"]

class PaymentGateway:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.transactions = {}
    
    def charge(self, amount: float, method: str, customer_email: str) -> dict:
        """
        Process a payment charge.
        BUG: 'crypto' is not in SUPPORTED_METHODS but the error message is misleading.
        """
        logger.info(f"Charging {amount} via {method} for {customer_email}")
        
        if method not in SUPPORTED_METHODS:
            # BUG: This raises a generic Exception instead of a specific one
            raise Exception(f"Unsupported payment method: {method}. Use one of {SUPPORTED_METHODS}")
        
        if amount <= 0:
            raise ValueError(f"Charge amount must be positive, got {amount}")
        
        # Simulate API call
        transaction_id = str(uuid.uuid4())[:8]
        
        self.transactions[transaction_id] = {
            "amount": amount,
            "method": method,
            "email": customer_email,
            "status": "charged"
        }
        
        logger.info(f"Payment successful: txn={transaction_id}")
        
        return {
            "success": True,
            "transaction_id": transaction_id,
            "error": None
        }
    
    def refund(self, transaction_id: str) -> dict:
        """Refund a transaction. BUG: doesn't handle missing transaction_id."""
        txn = self.transactions[transaction_id]  # KeyError if not found
        txn["status"] = "refunded"
        return {"success": True, "refunded_amount": txn["amount"]}
