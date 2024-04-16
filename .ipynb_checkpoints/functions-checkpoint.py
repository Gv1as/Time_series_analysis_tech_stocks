import numpy as np
import pandas as pd

def calculate_technical_indicators(df):
    # Create a new DataFrame to store the calculated indicators
    indicators_df = pd.DataFrame(index=df.index)

    # Calculate Exponential Moving Averages (EMA)
    indicators_df['ema_12'] = df['Close'].ewm(span=12, adjust=False).mean()
    indicators_df['ema_26'] = df['Close'].ewm(span=26, adjust=False).mean()

    # Calculate Moving Average Convergence Divergence (MACD)
    indicators_df['macd_line'] = indicators_df['ema_12'] - indicators_df['ema_26']
    indicators_df['macd_signal'] = indicators_df['macd_line'].ewm(span=9, adjust=False).mean()

    # Calculate Relative Strength Index (RSI)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    indicators_df['rsi'] = 100 - (100 / (1 + rs))

    # Merge the calculated indicators DataFrame with the original DataFrame
    df = pd.concat([df, indicators_df], axis=1)

    return df