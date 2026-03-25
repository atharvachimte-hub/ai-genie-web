from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# 🔥 HOME PAGE FIX
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

def command_engine(command):

    command = command.lower()

    if any(word in command for word in ["open chrome", "chrome kholo", "chrome open"]):
        return "Chrome manually open kar"

    elif any(word in command for word in ["search", "khoj", "dhund"]):
        query = command.replace("search", "")
        return f"https://www.google.com/search?q={query}"

    elif any(word in command for word in ["time", "vel", "samay"]):
        return f"Time aahe {datetime.now().strftime('%H:%M')}"

    elif any(word in command for word in ["billing", "invoice"]):
        return "Billing software 7 divas madhe ready 💰"

    elif any(word in command for word in ["website", "web"]):
        return "Premium website 2 divas madhe ready 🔥"

    elif any(word in command for word in ["reel", "video"]):
        return "Reel ready flow 💰"

    else:
        return "Simple bol, samjat nahi ❌"

@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    command = data.get("command")

    response = command_engine(command)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
