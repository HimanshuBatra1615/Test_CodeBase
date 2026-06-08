"""
Inventory Manager — tracks product stock levels
"""
import logging

logger = logging.getLogger(__name__)

# Simulated database
STOCK_DB = {
    "WIDGET-A": 100,
    "GADGET-B": 5,
    "GIZMO-C": 0,
}

class InventoryManager:
    def __init__(self):
        self.stock = STOCK_DB.copy()
    
    def check_stock(self, sku: str) -> int:
        """Check available stock for a SKU."""
        if sku not in self.stock:
            raise KeyError(f"Unknown SKU: {sku}")
        return self.stock[sku]
    
    def reserve(self, sku: str, quantity: int) -> bool:
        """Reserve stock for an order."""
        available = self.check_stock(sku)
        if quantity > available:
            return False
        self.stock[sku] -= quantity
        logger.info(f"Reserved {quantity}x {sku}, remaining: {self.stock[sku]}")
        return True
    
    def get_all_stock(self) -> dict:
        """Return current stock levels."""
        return self.stock.copy()
