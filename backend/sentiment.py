from transformers import pipeline

print("Loading FinBERT model...")
sentiment_pipeline = pipeline("text-classification",model="ProsusAI/finbert",tokenizer="ProsusAI/finbert")

def analyze_sentiment(text):
    text = text[:512]
    try:
        results = sentiment_pipeline(text,top_k=None)
        scores = {r["label"]: r["score"] for r in results}
        
        positive = scores.get("positive",0)
        negative = scores.get("negative",0)
        neutral = scores.get("neutral",0)

        final_score = positive - negative

        dominant = max(scores,key=scores.get)

        return {
            "score": round(final_score, 3),
            "label": dominant,
            "positive": round(positive, 3),
            "negative": round(negative, 3),
            "neutral": round(neutral, 3)
        }

    except Exception as e:
        print(f"Sentiment error: {e}")
        return {"score": 0.0, "label": "neutral", "positive": 0, "negative": 0, "neutral": 1}


if __name__ == "__main__":
    test_comments = [
        "RCKT is going to moon, expected FDA approval next week!",
        "This stock is a scam, avoid at all costs",
        "DNUT looking bullish, strong support at $8",
        "I lost all my money on this garbage stock",
        "Neutral on BYND, waiting to see earnings"
    ]
    
    for comment in test_comments:
        result = analyze_sentiment(comment)
        print(f"Score: {result['score']:+.3f} | {result['label']:8} | {comment[:60]}")