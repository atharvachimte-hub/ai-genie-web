from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 🔥 FIXED HOME ROUTE
@app.route("/")
def home():
    return send_file("index.html")

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

    else:
        return "Simple bol ❌"

@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    command = data.get("command")

    response = command_engine(command)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
