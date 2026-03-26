from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# 🔑 OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🧠 SYSTEM PROMPT
SYSTEM_PROMPT = """
तू Omni AI आहेस — smart bhava tone मध्ये बोल.

Rules:
- Marathi + Hindi + simple English mix
- User input repeat करू नको
- Short, smart उत्तर दे
"""

# 🔥 OLD COMMAND ENGINE (UNCHANGED)
def command_engine(command):
    command = command.lower()

    if "chrome" in command:
        return "Chrome manually open kar bhava"

    elif "search" in command or "google" in command:
        query = command.replace("search", "")
        return f"https://www.google.com/search?q={query}"

    elif "time" in command:
        return f"Time aahe {datetime.now().strftime('%H:%M')}"

    return None  # IMPORTANT

# 🏠 HOME
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# 🤖 MAIN AI ROUTE
@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"reply": "बोल भावा, काय मदत करू?"})

    # 🔥 STEP 1: TRY COMMAND ENGINE
    command_result = command_engine(user_input)

    if command_result:
        return jsonify({"reply": command_result})

    # 🔥 STEP 2: AI RESPONSE
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )

    reply = response.choices[0].message.content.strip()

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
