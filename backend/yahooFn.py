import yfinance as yf

def enrich_with_price(results):
    for r in results:
        try:
            stock = yf.Ticker(r["ticker"])
            info = stock.info
            r["price"] = round(info.get("currentPrice") or info.get("regularMarketPrice") or 0, 2)
            r["change_percent"] = round(info.get("regularMarketChangePercent", 0), 2)
            r["market_cap"] = info.get("marketCap", 0)
            r["fifty_two_week_high"] = info.get("fiftyTwoWeekHigh", 0)
            r["fifty_two_week_low"] = info.get("fiftyTwoWeekLow", 0)
            r["volume"] = info.get("regularMarketVolume", 0)
            r["analyst_target"] = info.get("targetMeanPrice", 0)
            r["recommendation"] = info.get("recommendationKey", "none")
            r["sector"] = info.get("sector", "Unknown")
            r["description"] = info.get("longBusinessSummary", "")
        except Exception as e:
            print(f"Could not fetch price for {r['ticker']}: {e}")
            r["price"] = 0
            r["change_percent"] = 0
            r["market_cap"] = 0
            r["fifty_two_week_high"] = 0
            r["fifty_two_week_low"] = 0
            r["volume"] = 0
            r["analyst_target"] = 0
            r["recommendation"] = "none"
            r["sector"] = "Unknown"
            r["description"] = ""
    return results