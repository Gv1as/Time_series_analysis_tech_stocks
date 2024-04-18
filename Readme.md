# Stock Price Forecasting with ARIMA, SARIMA, and Prophet

## Project Overview
This repository contains the implementation and analysis of ARIMA, SARIMA, and Prophet models for forecasting stock prices of NVDA, AVGO, and TSM. The project aims to assess the efficacy of these time series forecasting models and to delve into the complexities of financial data. 

## Models Used
- **ARIMA (AutoRegressive Integrated Moving Average)**: Ideal for non-seasonal data.
- **SARIMA (Seasonal ARIMA)**: Enhances ARIMA by accounting for seasonal effects.
- **Prophet**: Developed by Facebook, adept at handling trend and seasonality.


## Methods and Fine-Tuning
### ARIMA and SARIMA
- **Hyperparameter Tuning**: Utilized grid search to optimize parameters such as p (lags), d (differencing), and q (moving average) for the models.
- **Seasonal Adjustments**: For SARIMA, additional tuning of seasonal parameters to better capture yearly and quarterly cycles.
- **Walk-Forward Validation**: Implemented to assess the model’s predictive accuracy by simulating a rolling forecasting scenario.

### Model Performance for Specific Stocks
- **NVDA**: The SARIMA (12) model with parameters `order=(4, 2, 2)`, `seasonal_order=(0, 0, 1, 12)` yielded the best results. Errors: **MSE**: 566.230, **MAPE**: 2.12%.
- **AVGO**: The SARIMA (4) model with parameters `order=(0, 1, 0)`, `seasonal_order=(0, 0, 1, 12)` was most effective. Errors: **MSE**: 1215.51, **MAPE**: 1.88%.
- **TSM**: The SARIMA (12) model with parameters `order=(0, 1, 2)`, `seasonal_order=(1, 0, 1, 12)` performed optimally. Errors: **MSE**: 11.46, **MAPE**: 1.93%.

## Methods and Fine-Tuning
### Prophet
- **Parameter Adjustment**: Focused on fine-tuning the changepoint sensitivity to better adapt to sudden changes in the trend.
- **Box-Cox Transformation**: Applied to normalize the distribution of residuals, improving the model’s predictive accuracy.
- **Holiday Effects**: Integrated specific models for handling holidays and special events which significantly impact stock prices.

### Model Performance for Specific Stocks
- **NVDA Stock**:
  - **Hyperparameter Tuning**: `{'changepoint_prior_scale': 0.1, 'seasonality_prior_scale': 0.01}`
  - **Box-Cox Transformation**: Applied to normalize the distribution of residuals.
  - **Errors**: MAE: 11.31, MAPE: 4.53%

- **TSM Stock**:
  - **Hyperparameter Tuning**: `{'changepoint_prior_scale': 0.1, 'seasonality_prior_scale': 0.01}`
  - **Errors**: MAE: 3.36, MAPE: 3.79%

- **AVGO Stock**:
  - **Hyperparameter Tuning**: `{'changepoint_prior_scale': 0.5, 'seasonality_prior_scale': 0.01}`
  - **Errors**: MAE: 15.79, MAPE: 2.99%


## Key Findings
- All models were enhanced significantly through parameter tuning and data transformation, reducing error metrics such as MSE, MAE and MAPE.
- While improvements were notable, challenges persisted with volatile stocks, affecting prediction reliability.
- ARIMA and SARIMA saw a growing uncertainty after each forecast point.
- Prophet was found to perform better for long-term forecasts, highlighting its utility for broader forecasting tasks.

## Conclusions
- The project demonstrated the value and limitations of ARIMA, SARIMA, and Prophet in the stock price forecasting domain.
- Continuous model evaluation and refinement are crucial for dealing with the inherent unpredictability of stock markets.
- Future work will explore integrating these models with machine learning techniques to potentially enhance prediction accuracy and handle complex patterns more effectively.

## Presentation slides
- (https://my.visme.co/view/epr8ozqv-untitled-project)

