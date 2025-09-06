from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load Hugging Face sentiment analyzer
sentiment_analyzer = pipeline("sentiment-analysis")

def get_response(user_input: str) -> str:
    result = sentiment_analyzer(user_input)[0]
    mood = result['label']

    if mood == "NEGATIVE":
        return "I hear you. It sounds like you’re feeling low. Want to try a breathing exercise?"
    elif mood == "POSITIVE":
        return "That’s wonderful! Keep going, you’re doing amazing ✨"
    else:
        return "Thanks for sharing. Remember, I’m here to listen."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = get_response(user_message)
    return jsonify({"reply": reply})

@app.route("/mood", methods=["POST"])
def mood():
    data = request.get_json()
    user_message = data.get("message", "")
    result = sentiment_analyzer(user_message)[0]
    return jsonify({
        "mood": result['label'],
        "score": result['score']
    })


if __name__ == "__main__":
    app.run(debug=True)
