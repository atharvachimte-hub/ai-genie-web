from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import webbrowser
import os

app = Flask(__name__)
CORS(app)

# Home route
@app.route("/")
def home():
    return send_from_directory("templates", "index.html")

# AI route
@app.route("/ai", methods=["POST"])
def ai():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"response": "No data received"})

        message = data.get("message", "").lower()

        # 🔥 BASIC COMMANDS
        if "hello" in message:
            reply = "Hello bhava 👑 Omni AI ready aahe!"

        elif "time" in message:
            now = datetime.now().strftime("%H:%M")
            reply = f"Time aahe {now}"

        elif "good morning" in message:
            reply = "Good morning bhava 🔥 full focus mode today!"

        # 🚀 AUTOMATION COMMANDS
        elif "open youtube" in message:
            webbrowser.open("https://youtube.com")
            reply = "YouTube open kelay bhava 🔥"

        elif "open google" in message:
            webbrowser.open("https://google.com")
            reply = "Google open kelay 🚀"

        elif "open calculator" in message:
            try:
                os.system("calc")  # Windows
            except:
                os.system("gnome-calculator")  # Linux fallback
            reply = "Calculator open kelay 🧮"

        else:
            reply = f"Tu mhanlas: {message}"

        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

# Render fix
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
