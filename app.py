from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ai", methods=["POST"])
def ai():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"response": "No data received"})

        message = data.get("message", "").lower()

        if "hello" in message:
            reply = "Hello bhava 👑 Omni AI ready aahe!"
        
        elif "time" in message:
            now = datetime.now().strftime("%H:%M")
            reply = f"Time aahe {now}"
        
        elif "good morning" in message:
            reply = "Good morning bhava 🔥 full focus mode today!"

        else:
            reply = f"Tu mhanlas: {message}"

        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

# IMPORTANT FOR RENDER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
