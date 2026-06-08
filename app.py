"""
E-Commerce Order Processing Application
Main entry point
"""
import logging
from order_service import OrderService
from payment_gateway import PaymentGateway
from utils.validators import validate_email, validate_order_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Order Processing System v2.1.0")
    
    gateway = PaymentGateway(api_key="sk_test_abc123")
    service = OrderService(gateway)
    
    # Process a batch of incoming orders
    orders = [
        {"id": "ORD-001", "customer_email": "alice@example.com", "items": [{"sku": "WIDGET-A", "qty": 2, "price": 29.99}], "payment_method": "credit_card"},
        {"id": "ORD-002", "customer_email": None, "items": [{"sku": "GADGET-B", "qty": 1, "price": 149.50}], "payment_method": "credit_card"},
        {"id": "ORD-003", "customer_email": "bob@example.com", "items": [], "payment_method": "paypal"},
        {"id": "ORD-004", "customer_email": "charlie@test.com", "items": [{"sku": "GIZMO-C", "qty": -1, "price": 75.00}], "payment_method": "crypto"},
    ]
    
    for order in orders:
        try:
            result = service.process_order(order)
            logger.info(f"Order {order['id']} processed: {result}")
        except Exception as e:
            logger.error(f"Failed to process order {order['id']}: {e}")

    logger.info("Batch processing complete")

if __name__ == "__main__":
    main()
