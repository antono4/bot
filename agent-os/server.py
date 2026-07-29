"""Agent OS - Flask Backend Server"""
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    history = data.get("history", [])
    
    if not os.getenv("OPENAI_API_KEY"):
        return jsonify({"error": "API key not set"})
    
    try:
        messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
        for h in history:
            messages.append({"role": h.get("role", "user"), "content": h.get("content", "")})
        messages.append({"role": "user", "content": message})
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
        
        return jsonify({
            "response": response.choices[0].message.content
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
