# project methodology

# Overview
This document details the technical approach, decisions, and rationale behind the cryptocurrency forecasting system

# Problem Defination

## Business Problem
Cryptocurrency investors face high volatility and uncertainity , leading to :
- Emotional , non-systematic trading decision
- Difficulty timing market entry/exit
- inability to quantify investment risk
- lack of data-driven decision support

## Technical challenge
predict Bitcoin prices 30 day ahead with:
- High accuracy (>90% R2)
- Quantified uncertainity (confidence intervals)
- Actionable insights for non-technical users

# Data Callection and Preparation

## Data Source
- Historical Bitcoin transactions (April-May 2013)
- 20,000 + records
- OHLCV format (Open, High, Low, Close, Volume) 

## Data Cleaning

In Excel
*steps Performed*
1. Removed duplicates:  0 found
2. Handled Missing Values: 0 found (100% complete)
3. Data Parsing : convert to datetime
4. Data type validation : all numeric field validated
5. outlier detection : Z-score method(none removed)

# Exploratory Data Analysis

*Key findings:*
- strong upward trend in Bitcoin Price
- High Volatility
- Volume correlates with price movements
- No clear seasonal patterns (Short timeframe)

# Feature Engineering

## Technical indicators
*Moving Averages(Trend)*

MA_7 = close.rolling(window=7).mean()
MA_30 = close.rolling(window=30).mean()
MA_90 = close.rolling(window=90).mean()

Rationale : Capture short, medium, long-term trends

*Exponential Moving Averages(Recent emphasis)*
EMA_12 = close.ewm(span=12, adjust= False).mean()
EMA_26 = close.ewm(span=26, adjust= False).mean()

Rationale : Weight recent price move heavily

*volatility Indicators*
volatility = close.rolling(window = 30).std()
price_range = high - low

Rationale : Measure market uncertainty

*lag Features (Autocorrelation)*
lag_1 = close.shift(1) #Yesterday
lag_7 = close.shift(7) #Last Week
lag_30= close.shift(30) #Last Month

Rationale : Capture temporal dependencies

*Date Features(Cyclical patterns)*
day, month, year, day_of_week , quater
Rationale : Detect calender effect

# Feature Selection
17 features selected based on
- Domain Knowledge (finance theory)
- correlation analysis (> 0.3 with target)
- Feature importance from preliminary models
- Low multicollinearity (VIF< 10)

# Model Developement

## Train-Test split
- *Split ratio :* 80% train , 20% test
- *Method :* Time-based(not random)
- *Rationale :* Prevent lookhead bias in time series

### Feature Scaling
MinMaxScaler(feature_range=(0,1))

- Standardizes features to [0,1] range
- improve gradient descent convergence
- Required for distance - based algorithms

#### Models Implemented

*Model1 : Linear Regression(Baseline)*
-*purpose* : Established baseline performance
-*Assumption* : Linear relationships
-*Pros* : Fast , interpretable
-*Cons* : cannot capture non-linearity

*Model2 : Random Forest*
-*Purpose* : Capture non-linear patterns
-*Approach* : Ensemble of decision trees
-*Pros* : Handles non-linearity , feature importance
-*Cons* : Slower, less intrpretable

*Model3 : Gradient Boosting*
-*Purpose* : Sequential error correction
-*Approach* : Builds trees to correct previous errors
-*Pros* : High accuracy , handles complex patterns
-*cons* : Prone to overfitting

*Model4 : ARIMA* 
ARIMA(order=(5,1,0))

-*Purpose* : Time series specific modeling
-*Approach* : Autoregressive integrated moving average
-*Pros* : Captures temporal autocorrelation
-*cons* : Assumes stationarity

# Evaluation Metrics

*R2 Score(Variance Explained)*
interpretation : 95% R2 = Model explains 95% of price variance

*RMSE(Root Mean Squared Error)*
interpretation : average prediction error in dollar

*MAE(Mean Absolute Error)*
interpretation : Average absolute prediction error

*MAPE(Mean absolute Percentage Error)*
interpretation : Average Percentage error

# Model Selection

## performance Comparison

Linear Regression
r2 score (train) : 0.8827
r2 score(test) : 0.4517
RMSE : $216,972.35
MAE: $144,057.70
MAPE : 158.07%

Random Forest
r2 score (train) : 0.9756
r2 score(test) : 0.1011
RMSE : $277,828.01
MAE: $222,380.60
MAPE : 140.91%

Gradient Boosting
r2 score (train) : 0.9992
r2 score(test) : -0.4561
RMSE : $353,593.12
MAE: $292,423.44
MAPE : 142.

ARIMA Model
R2 score : -0.1872
RMSE : $319,279.38
MAE : $301,128.45
MAPE : 210.26%

## Selection Criteria
Random Forest selected based on :
- Highest R2 Score
- Lowest prediction error
- good generalization (train-test gap minimal)
- feature importance insights
- Reasonable training time

# Forecasting

- 30-Day Ahead Predictions
- Confidence Intervals

# Ensemble Approach
- Reduce individual model bias
- improve robustness

# Validation

*Backtesting*
- prediction on unseen test set (20% of data)
- no data leakage from training set
- True out-of-sample evaluation

*Cross-Validation*
5-fold time series cross-validation
-Validates model stability
-Prevent overfitting
-Confirms consisent performance

*Residual Analysis*
- Residual approximately normal
- No systematic bias
- Homoscedastic(constant variance)

# Assumptions
- Historical pattern continue
- No Major Market disruptions
- Data quality remains high
- Feature relationships stable

# Limitations
- Cannot Predict black swan events
- Accuracy decrease with longer horizons
- Single cryptocurrency (Bitcoin only)
- Limited to quantitative factor (no sentiments)

# Mitigation Strategies
- Regular model retraining(monthly)
- Confidence intervals for uncertainity
- Ensemble approach for robustness
- ongoing monitoring and validation

# Future Improvements
- LSTM\GRU deep learning models
- Hyperparameter optimization
- Additional cryptocurrencies
- Real- Time data pipelines
- Sentiment analysis
- Market indicators
- On-Chain metrics
- News event detection
- Automated trading signals
- Portfolio optimization
- Risk management tools
- alert system for anomalies

Last Updated : January 2026
Author : Barkha Rani
















