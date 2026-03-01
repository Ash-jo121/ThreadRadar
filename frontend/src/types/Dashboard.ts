export interface TickerData {
  stockName: string;
  stockPrice: number;
  mentions: number;
  averageSentiment: number;
  finalScore: number;
  topContexts: TopContext[];
}

export interface TopContext {
  text: string;
  sentiment: number;
  score: number;
}
