"""Web Search Module"""
import requests

class WebSearch:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
    
    def search(self, query):
        try:
            url = f"https://duckduckgo.com/html/?q={requests.utils.quote(query)}"
            resp = requests.get(url, headers=self.headers, timeout=10)
            # Simple extraction
            if resp.status_code == 200:
                return f"Search results for \'{query}\':\n\n[See browser for full results]"
            return f"HTTP {resp.status_code}"
        except Exception as e:
            return f"Error: {e}"
