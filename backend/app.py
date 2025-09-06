from transformers import pipeline

# Load pre-trained sentiment analysis model
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

if __name__ == "__main__":
    print("MindMate AI is running. Type something to chat (Ctrl+C to quit).\n")
    while True:
        text = input("You: ")
        reply = get_response(text)
        print("MindMate:", reply)
