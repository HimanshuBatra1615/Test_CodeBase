"""
Order Service — handles order validation, enrichment, and processing
"""
import logging
from utils.validators import validate_email, validate_order_data
from inventory_manager import InventoryManager

logger = logging.getLogger(__name__)

class OrderService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway
        self.inventory = InventoryManager()
        self.processed_orders = {}

    def process_order(self, order_data: dict) -> dict:
        """Full order processing pipeline."""
        logger.info(f"Processing order {order_data.get('id')}")
        
        # Step 1: Validate
        validate_order_data(order_data)
        
        # Step 2: Validate email — BUG: doesn't check for None before calling
        email = order_data["customer_email"]
        if not validate_email(email):
            raise ValueError(f"Invalid email: {email}")
        
        # Step 3: Check inventory
        for item in order_data["items"]:
            available = self.inventory.check_stock(item["sku"])
            if available < item["qty"]:
                raise RuntimeError(f"Insufficient stock for {item['sku']}")
        
        # Step 4: Calculate total — BUG: no guard against empty items list
        total = self._calculate_total(order_data["items"])
        
        # Step 5: Charge payment
        charge_result = self.payment_gateway.charge(
            amount=total,
            method=order_data["payment_method"],
            customer_email=email
        )
        
        if not charge_result["success"]:
            raise RuntimeError(f"Payment failed: {charge_result['error']}")
        
        # Step 6: Store
        self.processed_orders[order_data["id"]] = {
            "status": "completed",
            "total": total,
            "transaction_id": charge_result["transaction_id"]
        }
        
        return self.processed_orders[order_data["id"]]
    
    def _calculate_total(self, items: list) -> float:
        """Calculate order total. BUG: negative qty not handled."""
        total = 0.0
        for item in items:
            subtotal = item["qty"] * item["price"]
            total += subtotal
        
        if total <= 0:
            raise ValueError(f"Order total must be positive, got {total}")
        
        return round(total, 2)
    
    def get_order(self, order_id: str) -> dict:
        """Retrieve a processed order."""
        return self.processed_orders[order_id]  # BUG: KeyError if not found
