import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline

# Define request body
class ChatRequest(BaseModel):
    user_id: str
    message: str

# Initialize FastAPI
app = FastAPI()

# Load model once at startup
# Using distilbert for sentiment analysis (lightweight)
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    # Analyze sentiment
    sentiment = sentiment_analyzer(request.message)[0]
    return {
        "user_id": request.user_id,
        "message": request.message,
        "sentiment": sentiment
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render requires binding to $PORT
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
