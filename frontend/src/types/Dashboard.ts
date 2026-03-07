export interface TickerData {
  stockName: string;
  mentions: number;
  averageSentiment: number;
  finalScore: number;
  topContexts: TopContext[];
  price: number;
  changePercent: number;
  marketCap: number;
  fiftyTwoWeekHigh: number;
  fiftyTwoWeekLow: number;
  volume: number;
  analystTarget: number;
  recommendation: string;
  sector: string;
  description: string;
}

export interface TopContext {
  text: string;
  sentiment: number;
  score: number;
}
