import os
from dotenv import load_dotenv
load_dotenv()

MODEL = os.getenv("MODEL", "gpt-4")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))
SAVE_HISTORY = True
HISTORY_FILE = "chat_history.json"
