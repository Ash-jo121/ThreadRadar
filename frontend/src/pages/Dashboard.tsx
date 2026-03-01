import { useEffect, useState } from "react";
import TickerRow from "../components/TickerRow";
import type { TickerData } from "../types/Dashboard";
import "../styles/Dashboard.css";

const API_URL = "http://localhost:8000/api/tickers";

export default function Dashboard() {
  const [tickerData, setTickerData] = useState<TickerData[]>([]);

  const fetchData = async () => {
    const response = await fetch(API_URL);
    const data = await response.json();
    const mapped: TickerData[] = data.map((item: any) => ({
      stockName: item.ticker,
      stockPrice: 0,
      mentions: item.mentions,
      averageSentiment: item.avg_sentiment,
      finalScore: item.final_score,
      topContexts: item.top_contexts,
    }));
    setTickerData(mapped);
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <h2>Top Stock Picks</h2>
      <table className="dashboard-table">
        <tr>
          <th>Stock</th>
          <th>Price</th>
          <th>Mentions</th>
          <th>Avg Sentiment</th>
          <th>Final Score</th>
        </tr>
        {tickerData.map((item) => (
          <TickerRow tickerData={item} />
        ))}
      </table>
    </div>
  );
}
