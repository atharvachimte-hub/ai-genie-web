from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ai_engine import process_command

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory("templates", "index.html")

@app.route("/ai", methods=["POST"])
def ai():
    data = request.get_json()
    message = data.get("message", "")

    reply = process_command(message)

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
