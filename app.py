from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
तू Omni AI आहेस — smart, friendly bhava tone मध्ये बोल.

Rules:
- Marathi + Hindi + simple English mix
- User input repeat करू नको
- Short, smart, useful उत्तर दे
- Human सारखं बोल

काम:
- software ideas
- billing system
- business help
- automation
"""

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"reply": "बोल भावा, काय मदत करू?"})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0.8
    )

    reply = response.choices[0].message.content.strip()

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
