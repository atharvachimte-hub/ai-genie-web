from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# 🔑 OpenAI Setup
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🧠 SYSTEM PROMPT (MAIN BRAIN)
SYSTEM_PROMPT = """
तू एक smart AI assistant आहेस (Omni AI / Jarvis level)

Rules:
- Always reply in smooth Marathi + Hindi + simple English mix
- Never repeat user input
- Think and give helpful, practical answer
- Keep answer short, smart, actionable
- Sound like friendly bhava tone 👑
- Avoid robotic tone

Capabilities:
- Prompt generation (image/video/reels)
- Billing software ideas
- Business suggestions
- Automation help
"""

@app.route("/ai", methods=["POST"])
def ai():
    try:
        data = request.json
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"reply": "काय मदत करू भावा?"})

        # 🧠 REAL AI CALL
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=300
        )

        ai_reply = response.choices[0].message.content.strip()

        return jsonify({"reply": ai_reply})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"reply": "थोडा issue आला भावा, परत try कर 🙏"})
        

if __name__ == "__main__":
    app.run(debug=True)
