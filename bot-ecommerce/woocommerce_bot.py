"""WooCommerce Bot - E-commerce automation for WooCommerce"""
import os
import logging
from woocommerce import API

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WooCommerceBot:
    def __init__(self):
        self.url = os.getenv("WOOCOMMERCE_URL")
        self.consumer_key = os.getenv("WOOCOMMERCE_KEY")
        self.consumer_secret = os.getenv("WOOCOMMERCE_SECRET")
        self.wcapi = None
        logger.info("WooCommerce Bot initialized")
    
    def connect(self):
        self.wcapi = API(
            url=self.url,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            version="wc/v3"
        )
        logger.info(f"Connected to WooCommerce: {self.url}")
    
    def get_products(self, per_page=100):
        logger.info(f"Getting products (per_page={per_page})")
        return self.wcapi.get("products", params={"per_page": per_page}).json()
    
    def get_orders(self, status=None):
        params = {}
        if status:
            params["status"] = status
        logger.info(f"Getting orders with status: {status}")
        return self.wcapi.get("orders", params=params).json()
    
    def update_inventory(self, product_id, quantity):
        logger.info(f"Updating inventory for product {product_id}: {quantity}")
        data = {"regular_price": str(quantity)}
        return self.wcapi.put(f"products/{product_id}", data=data).json()

def main():
    bot = WooCommerceBot()
    bot.connect()
    products = bot.get_products()
    print(f"Found {len(products)} products")

if __name__ == "__main__":
    main()
