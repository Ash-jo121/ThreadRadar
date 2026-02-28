import json
from scraper import fetch_all
from extractor import aggregate_tickers,extract_from_post
from sentiment import analyze_sentiment

def analyze_ticker_sentiment(all_posts):
    master = {}

    for post in all_posts:
        found = extract_from_post(post)

        for ticker,data in found.items():
            if ticker not in master:
                master[ticker] = {
                    "mentions":0,
                    "sentiment_scores":[],
                    "contexts":[],
                    "post_scores":[]
                }

            master[ticker]["mentions"] += data["mentions"]
            master[ticker]["post_scores"].append(post["score"])

            for context in data["contexts"]:
                sentiment = analyze_sentiment(context)
                master[ticker]["sentiment_scores"].append(sentiment["score"])
                master[ticker]["contexts"].append({
                    "text":context[:150],
                    "sentiment":sentiment["label"],
                    "score":sentiment["score"]
                }) 

    results = []
    for ticker,data in master.items():
        if data["mentions"] < 1:
            continue

        avg_sentiment = (
            sum(data["sentiment_scores"]) / len(data["sentiment_scores"])
            if data["sentiment_scores"] else 0
        )

        avg_post_score = (
            sum(data["post_scores"]) / len(data["post_scores"])
            if(data["post_scores"]) else 0
        )

        final_score = avg_sentiment * (1 + data["mentions"] * 0.1) * (1 + avg_post_score *0.01)

        results.append({
            "ticker":ticker,
            "mentions":data["mentions"],
            "avg_sentiment":round(avg_sentiment,3),
            "final_score":round(final_score,3),
            "top_contexts":data["contexts"][:3]
        })
    
    results.sort(key=lambda x: x["final_score"], reverse=True)
    results = [r for r in results if r["mentions"] >= 2]
    return results


if __name__ == "__main__":
    print("=== ThreadRadar ===\n")

    print("Step 1: Fetching posts...")
    posts = fetch_all()

    print("\nStep 2: Analyzing tickers and sentiment...")
    results = analyze_ticker_sentiment(posts)

    print("\n=== TOP STOCK PICKS ===\n")

    with open("output.json", "w",encoding="utf-8") as file:
        json.dump(results[:10], file, indent=2,ensure_ascii=False)
    
    with open("output.txt", "w",encoding="utf-8") as file:
        for r in results[:10]:
            file.write(f"${r['ticker']}\n")
            file.write(f"  Mentions: {r['mentions']} | Sentiment: {r['avg_sentiment']:+.3f} | Score: {r['final_score']:+.3f}\n")
            file.write(f"  Context: {r['top_contexts'][0]['text'][:100] if r['top_contexts'] else 'N/A'}\n")
            file.write("\n")  # blank line between stocks