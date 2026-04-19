"use client"

import { useEffect, useState } from "react"

interface ExchangeRateResponse {
  rates: { [key: string]: number };
  base: string;
  date: string;
}

export default function Home() {
  const [area, setArea] = useState("")
  const [quality, setQuality] = useState("")
  const [year, setYear] = useState("")
  const [result, setResult] = useState<number | null>(null)
  const [exchangeRate, setExchangeRate] = useState<number | null>(null)

  const handlePredict = async () => {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        LotArea: Number(area),
        OverallQual: Number(quality),
        YearBuilt: Number(year),
      }),
    });

    const data = await res.json()
    setResult(data.prediction)
  };

  const getUSDToVND = async () => {
    const response = await fetch("https://api.exchangerate-api.com/v4/latest/USD");
    const data: ExchangeRateResponse = await response.json();
    const rate = data.rates["VND"];
    setExchangeRate(rate);
    return rate;
  };

  useEffect(() => {
    getUSDToVND();
  }, []);

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold mb-4">
        House Price Prediction
      </h1>

      <input
        placeholder="Lot Area"
        className="border p-2 mr-2"
        onChange={(e) => setArea(e.target.value)}
      />

      <input
        placeholder="Overall Quality"
        className="border p-2 mr-2"
        onChange={(e) => setQuality(e.target.value)}
      />

      <input
        placeholder="Year Built"
        className="border p-2 mr-2"
        onChange={(e) => setYear(e.target.value)}
      />

      <button
        className="bg-blue-500 text-white p-2 rounded"
        onClick={handlePredict}
      >
        Predict
      </button>

      {result !== null && (
        <div className="mt-4">
          <h2 className="text-xl font-bold">Prediction Price in USD: ${result}</h2>
          <h2 className="text-xl font-bold">Prediction Price in VND: {result * (exchangeRate || 0)} VND</h2>
        </div>
      )}
    </div>
  )
}