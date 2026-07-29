"""OpenHands Agent Bot"""
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpenHandsBot:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("LLM_MODEL", "gpt-4")
        logger.info("OpenHands Bot initialized")
    
    def run_task(self, task_description):
        logger.info(f"Running task: {task_description}")

def main():
    bot = OpenHandsBot()
    print("OpenHands Bot ready!")

if __name__ == "__main__":
    main()
