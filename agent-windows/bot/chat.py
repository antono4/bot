"""AI Chat Module"""
import os

try:
    import openai
    OPENAI_AVAILABLE = True
except:
    OPENAI_AVAILABLE = False

class ChatBot:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("MODEL", "gpt-4")
        
        if self.api_key and OPENAI_AVAILABLE:
            self.client = openai.OpenAI(api_key=self.api_key)
    
    def ask(self, question, history=None):
        if not self.api_key:
            return "Set OPENAI_API_KEY in .env file"
        
        try:
            messages = (history or [{"role": "user", "content": question}])
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
