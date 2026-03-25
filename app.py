from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__, static_folder=".")
CORS(app)

# ✅ DIRECT FILE LOAD (NO PATH ISSUE)
@app.route("/")
def home():
    return send_file("index.html")

# 🔥 COMMAND ENGINE
def command_engine(command):

    command = command.lower()

    if "search" in command:
        return "Search working 🚀"

    elif "time" in command:
        return f"Time aahe {datetime.now().strftime('%H:%M')}"

    elif "billing" in command:
        return "Billing software ready 💰"

    elif "website" in command:
        return "Website ready 🔥"

    elif "reel" in command:
        return "Reel system ready 🎬"

    else:
        return "Simple bol ❌"

# 🔥 API
@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    command = data.get("command")

    response = command_engine(command)

    return jsonify({"response": response})

# 🔥 STATIC FILE SUPPORT (IMPORTANT)
@app.route("/<path:path>")
def static_files(path):
    return send_file(path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
