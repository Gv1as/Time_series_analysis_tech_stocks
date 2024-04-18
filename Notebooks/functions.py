import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller
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

    df = pd.concat([df, indicators_df], axis=1)

    return df

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def check_stationarity(ts):
    dftest = adfuller(ts)
    adf = dftest[0]
    pvalue = dftest[1]
    critical_value = dftest[4]['5%']
    if (pvalue < 0.05) and (adf < critical_value):
        print('The series is stationary')
    else:
        print('The series is NOT stationary')

def perform_adf_test(ts):
    adf_result = adfuller(ts)
    return adf_result