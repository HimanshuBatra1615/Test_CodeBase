"""
Validation utilities for order data and user inputs
"""
import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.
    BUG: Crashes with TypeError if email is None instead of returning False.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))  # TypeError if email is None


def validate_order_data(order: dict) -> None:
    """
    Validate order data structure.
    BUG: Doesn't check if 'items' list is empty.
    BUG: Doesn't validate item quantities are positive.
    """
    required_fields = ["id", "customer_email", "items", "payment_method"]
    
    for field in required_fields:
        if field not in order:
            raise ValueError(f"Missing required field: {field}")
    
    if not isinstance(order["items"], list):
        raise TypeError(f"'items' must be a list, got {type(order['items'])}")
    
    # NOTE: Missing check for empty items list!
    # NOTE: Missing check for negative quantities!


def sanitize_input(text: str) -> str:
    """Basic input sanitization."""
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text)}")
    return text.strip().replace("<", "&lt;").replace(">", "&gt;")
