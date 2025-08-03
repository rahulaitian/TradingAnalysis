def get_trade_signal(df):
    try:
        latest = df.iloc[-1]
        buy_signals = 0
        total_signals = 0

        def safe_get(name):
            try:
                return latest[name].item()
            except:
                return None

        buy_signals = 0
        total_signals = 0

        close = safe_get("close")

        # EMA
        ema_20 = safe_get("ema_20")
        ema_50 = safe_get("ema_50")
        ema_100 = safe_get("ema_100")
        if None not in (ema_20, ema_50, ema_100):
            total_signals += 1
            if ema_20 >= ema_50 >= ema_100:
                buy_signals += 1
            elif ema_20 < ema_50 < ema_100:
                buy_signals -= 1

        # SMA
        sma_50 = safe_get("sma_50")
        sma_200 = safe_get("sma_200")
        if None not in (sma_50, sma_200):
            total_signals += 1
            if sma_50 >= sma_200:
                buy_signals += 1
            elif sma_50 < sma_200:
                buy_signals -= 1

        # MACD
        macd = safe_get("macd")
        macd_signal = safe_get("macd_signal")
        if None not in (macd, macd_signal):
            total_signals += 1
            if macd > macd_signal:
                buy_signals += 1
            elif macd < macd_signal:
                buy_signals -= 1

        macd_diff = safe_get("macd_diff")
        if macd_diff is not None:
            total_signals += 1
            if macd_diff > 0:
                buy_signals += 1
            elif macd_diff < 0:
                buy_signals -= 1

        # ADX
        adx = safe_get("adx")
        if adx is not None:
            total_signals += 1
            if adx > 25 and close is not None and ema_50 is not None:
                if close > ema_50:
                    buy_signals += 1
            elif adx < 20:
                buy_signals -= 1

        # RSI
        rsi = safe_get("rsi")
        if rsi is not None:
            total_signals += 1
            if rsi < 30:
                buy_signals += 1
            elif rsi > 70:
                buy_signals -= 1

        # CCI
        cci = safe_get("cci")
        if cci is not None:
            total_signals += 1
            if cci < -100:
                buy_signals += 1
            elif cci > 100:
                buy_signals -= 1

        # Williams %R
        willr = safe_get("willr")
        if willr is not None:
            total_signals += 1
            if willr < -80:
                buy_signals += 1
            elif willr > -20:
                buy_signals -= 1

        # Stochastic RSI
        stochrsi = safe_get("stochrsi_k")
        if stochrsi is not None:
            total_signals += 1
            if stochrsi < 0.2:
                buy_signals += 1
            elif stochrsi > 0.8:
                buy_signals -= 1

        # MFI
        mfi = safe_get("mfi")
        if mfi is not None:
            total_signals += 1
            if mfi < 20:
                buy_signals += 1
            elif mfi > 80:
                buy_signals -= 1

        # Awesome Oscillator (AO)
        ao = safe_get("ao")
        if ao is not None:
            total_signals += 1
            if ao > 0:
                buy_signals += 1
            else:
                buy_signals -= 1

        # Keltner Channel breakout
        keltner_upper = safe_get("keltner_upper")
        keltner_lower = safe_get("keltner_lower")
        if None not in (keltner_upper, keltner_lower, close):
            total_signals += 1
            if close > keltner_upper:
                buy_signals += 1
            elif close < keltner_lower:
                buy_signals -= 1

        # Final Decision
        if total_signals == 0:
            return "Don't Touch this stock"

        buy_ratio = buy_signals / total_signals
        num = buy_ratio * 100

        if buy_ratio <= -0.4:
            return f"{num:.2f}% High selling opportunity"
        elif buy_ratio <= 0.4:
            return "Dont do anything"
        else:
            return f"{num:.2f}% so Watch List it"

    except Exception as e:
        print(f"⚠️ Signal generation error: {e}")
        return "ERROR"
