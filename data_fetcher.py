# data_fetcher.py

import yfinance as yf
import pandas as pd
import time
from config import DEFAULT_INTERVAL, DEFAULT_PERIOD

def get_stock_data(symbol, interval=DEFAULT_INTERVAL, period=DEFAULT_PERIOD, retries=3, delay=2):
    attempt = 0

    while attempt < retries:
        try:
            df = yf.download(
                tickers=symbol,
                interval=interval,
                period=period,
                auto_adjust=False,
                progress=False,
                threads=False  # important for stability
            )

            df.dropna(inplace=True)

            if df.empty or "Close" not in df.columns:
                raise ValueError(f"No valid data fetched for {symbol}")

            return df

        except Exception as e:
            attempt += 1
            print(f"⚠️ Attempt {attempt} failed for {symbol}: {e}")
            time.sleep(delay)

    print(f"❌ Skipped {symbol}: No data available after {retries} attempts")
    return pd.DataFrame()  # Return empty DataFrame if all retries fail
