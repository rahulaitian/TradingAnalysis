# indicators.py

import ta

def add_indicators(df):

    close_series = df["Close"].squeeze()
    high_series = df["High"].squeeze()
    low_series = df["Low"].squeeze()
    volume_series = df["Volume"].squeeze()

    print(type(df["Close"]), df["Close"].shape)

    df["ema_20"] = ta.trend.ema_indicator(close=close_series, window=20)
    df["ema_50"] = ta.trend.ema_indicator(close=close_series, window=50)
    df["ema_100"] = ta.trend.ema_indicator(close=close_series, window=100)

    df["sma_50"] = ta.trend.sma_indicator(close=close_series, window=50)
    df["sma_200"] = ta.trend.sma_indicator(close=close_series, window=200)

    df["macd"] = ta.trend.macd(close=close_series)
    df["macd_signal"] = ta.trend.macd_signal(close=close_series)
    df["macd_diff"] = ta.trend.macd_diff(close=close_series)

    df["adx"] = ta.trend.adx(high=high_series, low=low_series, close=close_series)
    df["cci"] = ta.trend.cci(high=high_series, low=low_series, close=close_series)
    df["dpo"] = ta.trend.dpo(close=close_series)
    df["kst"] = ta.trend.kst(close=close_series)

    df["rsi"] = ta.momentum.rsi(close=close_series)
    df["williams_r"] = ta.momentum.williams_r(high=high_series, low=low_series, close=close_series)
    df["ao"] = ta.momentum.awesome_oscillator(high=high_series, low=low_series)
    df["roc"] = ta.momentum.roc(close=close_series)
    df["kama"] = ta.momentum.kama(close=close_series)
    df["tsi"] = ta.momentum.tsi(close=close_series)
    df["stochrsi"] = ta.momentum.stochrsi(close=close_series)

    bb = ta.volatility.BollingerBands(close=close_series)
    df["bb_bbm"] = bb.bollinger_mavg()
    df["bb_bbh"] = bb.bollinger_hband()
    df["bb_bbl"] = bb.bollinger_lband()
    df["bb_bw"] = bb.bollinger_wband()
    df["bb_pband"] = bb.bollinger_pband()

    df["atr"] = ta.volatility.average_true_range(high=high_series, low=low_series, close=close_series)

    donchian = ta.volatility.DonchianChannel(high=high_series, low=low_series, close=close_series)
    df["donchian_hband"] = donchian.donchian_channel_hband()
    df["donchian_lband"] = donchian.donchian_channel_lband()
    df["donchian_mband"] = donchian.donchian_channel_mband()

    df["ulcer_index"] = ta.volatility.ulcer_index(close=close_series)

    df["obv"] = ta.volume.on_balance_volume(close=close_series, volume=volume_series)
    df["cmf"] = ta.volume.chaikin_money_flow(high=high_series, low=low_series, close=close_series, volume=volume_series)
    df["adi"] = ta.volume.acc_dist_index(high=high_series, low=low_series, close=close_series, volume=volume_series)
    df["eom"] = ta.volume.ease_of_movement(high=high_series, low=low_series, volume=volume_series)
    df["force_index"] = ta.volume.force_index(close=close_series, volume=volume_series)
    df["mfi"] = ta.volume.money_flow_index(high=high_series, low=low_series, close=close_series, volume=volume_series)
    df["nvi"] = ta.volume.negative_volume_index(close=close_series, volume=volume_series)

    vi = ta.trend.VortexIndicator(high=high_series, low=low_series, close=close_series)
    df["vi_plus"] = vi.vortex_indicator_pos()
    df["vi_minus"] = vi.vortex_indicator_neg()

    df["trix"] = ta.trend.trix(close=close_series)

    df["mass_index"] = ta.trend.mass_index(high=high_series, low=low_series)
    df["awesome_oscillator"] = ta.momentum.awesome_oscillator(high=high_series, low=low_series)
    df["keltner_channel_hband"] = ta.volatility.keltner_channel_hband(high=high_series, low=low_series,
                                                                      close=close_series)
    df["keltner_channel_lband"] = ta.volatility.keltner_channel_lband(high=high_series, low=low_series,
                                                                      close=close_series)

    return df
