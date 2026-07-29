"""Support Ticket Bot"""
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SupportBot:
    def __init__(self):
        self.zendesk_url = os.getenv("ZENDESK_URL")
        self.zendesk_token = os.getenv("ZENDESK_TOKEN")
        logger.info("Support Bot initialized")
    
    def get_tickets(self, status="open"):
        logger.info(f"Getting {status} tickets")
    
    def reply_ticket(self, ticket_id, message):
        logger.info(f"Replying to ticket {ticket_id}")

def main():
    bot = SupportBot()
    print("Support Bot ready!")

if __name__ == "__main__":
    main()
