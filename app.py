
from flask import Flask, request, jsonify
from bot_logic import get_bot_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    lang = request.json.get("lang", "en")
    response = get_bot_response(user_input, lang)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
