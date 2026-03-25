from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# AI route
@app.route("/ai", methods=["POST"])
def ai():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"response": "No message received"})

        user_message = data["message"].lower()

        # Basic command system
        if "hello" in user_message:
            reply = "Hello bhava 👑, Omni AI ready aahe!"
        
        elif "time" in user_message:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            reply = f"Current time aahe {now}"

        elif "open youtube" in user_message:
            reply = "YouTube open karaycha command backend madhe add karto next step madhe"

        elif "good morning" in user_message:
            reply = "Good morning bhava 🔥 aaj full focus mode madhe kaam karu!"

        else:
            reply = f"Tu mhanlas: {user_message} — me samjtoy, next upgrade madhe smart AI reply yenar"

        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": f"Error aala: {str(e)}"})

# Run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
