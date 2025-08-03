# main.py

import os
from data_fetcher import get_stock_data
from indicators import add_indicators
from signal_logic import get_trade_signal

def ensure_data_dir():
    if not os.path.exists("data"):
        os.makedirs("data")

if __name__ == "__main__":
    ensure_data_dir()

    # 🔁 Add your list of stocks here
    nifty_50_stocks = [
  "ADANIPORTS.NS", "ASIANPAINT.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS",
  "BAJAJFINSV.NS", "BHARTIARTL.NS", "BPCL.NS", "BRITANNIA.NS", "CIPLA.NS",
  "COALINDIA.NS", "DIVISLAB.NS", "DRREDDY.NS", "EICHERMOT.NS", "GRASIM.NS",
  "HCLTECH.NS", "HDFCBANK.NS", "HDFCLIFE.NS", "HEROMOTOCO.NS", "HINDALCO.NS",
  "HINDUNILVR.NS", "ICICIBANK.NS", "INDUSINDBK.NS", "INFY.NS", "ITC.NS",
  "JSWSTEEL.NS", "KOTAKBANK.NS", "LTIM.NS", "LT.NS", "M&M.NS",
  "MARUTI.NS", "NESTLEIND.NS", "NTPC.NS", "ONGC.NS", "POWERGRID.NS",
  "RELIANCE.NS", "SBILIFE.NS", "SBIN.NS", "SHREECEM.NS", "SUNPHARMA.NS",
  "TATACONSUM.NS", "TATAMOTORS.NS", "TATASTEEL.NS", "TCS.NS", "TECHM.NS",
  "TITAN.NS", "ULTRACEMCO.NS", "UPL.NS", "WIPRO.NS",
  "LICI.NS", "HAL.NS", "AvenueSupermarts.NS", "InterGlobeAviation.NS", "AdaniPower.NS",
  "IndianOil.NS", "Vedanta.NS", "AMBUJACEM.NS", "BajajHoldings.NS", "BHEL.NS",
  "BANKBARODA.NS", "BOSCHLTD.NS", "ZYDUSLIFE.NS", "CanaraBank.NS", "Cholamandalam.NS",
  "Dabur.NS", "DivisLab.NS", "DLF.NS", "GAIL.NS", "GodrejCP.NS",
  "Havells.NS", "InfoEdge.NS", "JindalSteel.NS", "JSWEnergy.NS", "NHPC.NS",
  "Pidilite.NS", "PowerFinance.NS", "PunjabNationalBank.NS", "REC.NS", "ShreeCem.NS",
  "Siemens.NS", "TataPower.NS", "TorrentPharma.NS", "TVSMotor.NS", "UnionBank.NS",
  "UnitedSpirits.NS", "AdaniEnergy.NS", "LTIMindtree.NS", "ICICIPruLife.NS", "VarunBev.NS"
]


    stock_list = nifty_50_stocks

    for symbol in stock_list:
        print(f"\n📥 Analyzing {symbol}...")

        df = get_stock_data(symbol)

        if df.empty:
            print(f"❌ Skipped {symbol}: No data available")
            continue

        try:
            df = add_indicators(df)
            signal = get_trade_signal(df)
            print(f"🔔 Signal for {symbol}: {signal}")
        except Exception as e:
            print(f"⚠️ Error analyzing {symbol}: {e}")
