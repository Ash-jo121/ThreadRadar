import { useEffect, useState } from "react";
import type { TickerData } from "../types/Dashboard";
import "../styles/Dashboard.css";
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "../components/ui/table";

const API_URL = "http://localhost:8000/api/tickers";

export default function Dashboard() {
  const [tickerData, setTickerData] = useState<TickerData[]>([]);

  const fetchData = async () => {
    const response = await fetch(API_URL);
    const data = await response.json();
    const mapped: TickerData[] = data.map((item: any) => ({
      stockName: item.ticker,
      mentions: item.mentions,
      averageSentiment: item.avg_sentiment,
      finalScore: item.final_score,
      topContexts: item.top_contexts,
      price: item.price,
      changePercent: item.change_percent,
      marketCap: item.market_cap,
      fiftyTwoWeekHigh: item.fifty_two_week_high,
      fiftyTwoWeekLow: item.fifty_two_week_low,
      volume: item.volume,
      analystTarget: item.analyst_target,
      recommendation: item.recommendation,
      sector: item.sector,
      description: item.description,
    }));
    setTickerData(mapped);
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="main-dashboard">
      <h1 className="scroll-m-20 text-center text-4xl font-extrabold tracking-tight text-balance">
        Welcome to ThreadRadar
      </h1>
      <h2 className="scroll-m-20 text-2xl font-semibold tracking-tight">
        Top 10 stocks
      </h2>
      <Table>
        <TableCaption>A list of all top stock picks</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead className="w-[100px]">Stock</TableHead>
            <TableHead className="w-[100px]">Price ($)</TableHead>
            <TableHead className="w-[100px]">Mentions</TableHead>
            <TableHead className="w-[200px]">Average Sentiment</TableHead>
            <TableHead className="w-[100px]">Final Score</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {tickerData.map((item) => (
            <TableRow key={item.stockName}>
              <TableCell className="font-medium">{item.stockName}</TableCell>
              <TableCell>{item.price}</TableCell>
              <TableCell>{item.mentions}</TableCell>
              <TableCell>{item.averageSentiment}</TableCell>
              <TableCell>{item.finalScore}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
