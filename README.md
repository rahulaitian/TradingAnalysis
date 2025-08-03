# 📊 Trading Signal Bot

This is a Python-based trading bot that analyzes stock data using over 35 technical indicators from the `ta` library. It generates Buy/Sell/Hold signals based on indicator consensus and supports multiple stock tickers.

---

## 🧠 Features

- ✅ Pulls historical data using `yfinance`
- ✅ Adds 35+ technical indicators (EMA, RSI, MACD, Bollinger, ATR, etc.)
- ✅ Robust signal logic: majority vote or threshold-based signal
- ✅ Multi-stock support (e.g., `INFY.NS`, `RELIANCE.NS`, etc.)
- ✅ Handles 1D and 2D indicators safely (via `.squeeze()` / `.iloc[-1]`)
- ✅ Graceful fallback for invalid indicators
- ✅ Optional: Save enriched data locally (CSV or DB) for further analysis

---

## 🗂️ Project Structure

