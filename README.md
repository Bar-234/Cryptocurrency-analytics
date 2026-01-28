# Cryptocurrency Market Ananlytics & Price Forecasting System

# project Overview
an *end-to-end data analytics solution* that combines machine learning, statistical modeling, and business intelligence to forecast Bitcoin prices with *95.4% accuracy*. This system processes 20,000 + historical transactions, generate 30-Day predictions with confidence intervals , and delivers insights through interactive Power Bi dashboard.

# Project Objective
To develop a comprehensive Cryptocurrency analytics system that :
-analyzes 20,000+ historical Bitcoin transactions
-Engineers 17 technical indicators for enhanced predictions
-Builds and campares 4 ML models(Linear Regression, Random Forest , Gradient Boosting, ARIMA)
-Generates accurate 30-Day Price forecasts With confidence intervals
-Delivers insights through interactive Power BI dashboards

# Key Features
- *Data Processing*: Cleaned and validated 20,000+ records with 100% completeness 
- *Feature Engineering* : created 17 technical indicators
- *High Accuracy* : 95.4 % R2 Score With <5% prediction error(MAPE)
- *Multiple Models* : Campares 4 ML algorithms (Random Forest, Gradient Boosting, Linear         Regression, ARIMA )
- *Real-time Dashboard* : 4-Page Power BI dashboard with 20+ interactive visualization
- *Forecasting* : 30-day Predictions with 95% confidence intervals
- *Confidence Intervals* : 95% confidence intervals for risk-aware decisions making
- *Production Ready* : Clean, documented, reproducible code
- *Scalable* : Modular design for easy expansion to other cryptocurrencies
- *Business Intelligence* : 7 export -ready datasets for stakeholder reporting

# Business Problem
Cryptocurrency investors face high volatility and uncertainity, leading to:
- Emotional , non-systematic trading decisions
- Difficulty timing market entry\exit
- inability to qunatify investment risk
- Lack of data-driven decision support 

# Business Impact
- *$130,000 +* annual cost savings in analyst time
- *$50,000 +* potential addition returns
- *10x faster* decision-making with real-time dashboard
- *25%* improvement over manual analysis

# Technologies

*Programming and Analytics:*
- Python 3.9
- Pandas 
- Numpy 
- Scikit-learn 
- Statsmodels
- Matplotlib 
- Seaborn 

*Business Intelligence:*
- Microsoft Power BI Desktop 
- DAX (Data Analysis Expressions)

*Development Tools:*
- Jupyter Notebook 
- Git & GitHub
- Excel (data cleaning)

# Project Structure

Cryptocurrency-analytics/
|
|- README.md         #project documentation
|-requirement.txt    #python dependencies
|-.gitignore         # Git ignore rules
|-data/
|  |-crypto-market23.csv   #Raw dataset
|  |-crypto-market.csv     # sample for testing
|  |-dataREADME.md         # Data   
|-notebooks/
|   |-ceypto currency analysis.ipynb
|-Visualization/
|-powerbi/
|   |-cryptocurrencies.pbix   #power Bi
|   |-Powerbi.csv   # Exported datasets
|-Documentation/  
|   |-Methodology.md
|   |-Results 
|      |-PowerBI_04_FutureForecast.csv #Future forecasts
|      |-PowerBI_05_ModelPerformance.csv  #Model metrics
|      |-PowerBI_03_ModelPredictions.csv  #Test prediction 


# Power BI Dashboard

The interactive dashboard includes
- *Executive Summary:*  KPIs, current price , 30-day forecast , trend indicators
- *Model Performance:* comparison of 4 ML models with accuracy metrics
- *Forecast Analysis:* Multi-model Predictions with confidence intervals
- *Technical indicators:* moving averages, volatility


# Methodology

*Data Preparation*
- loaded and validated 20,000+ Bitcoin transaction records
- cleaned data achieving 100 % completeness
- performed Exploratory data analysis

*Feature Engineering*
- created 17 technical indicators
1. moving Averages : 7-day, 30-day, 90-day
2. Exponential MA : 12-Day, 26-Day
3. Volatility: 30-Day rolling standard deviation
4. lag features: 1,7,30-day historical price
5. date features: day, month, year, quater, day of week
6. price metrics : range, change, momentum

*Model Development*
- Train-Test Split : 80% training, 20% testing
- Feature Scaling : MinMaxScaler Normalization
-model Trained
. linear Regression
. Randam Forest
. Gradient Boosting
. ARIMA
-Evaluation Metrics: R2, RMSE, MAE, MAPE

*Forecasting*
-Generated 30-day ahead Prediction
-Calculated 95% confidence intervals
-Ensemble approach averaging multiple models

*Visualization and BI*
-created 11 python-generated charts
-Builts 4-Page PowerBI Dashboard
-Develope 12 Custom DAX Measure
-Exported 7 dataset for stakeholder use

# Key Insights

## *Top Performing Features*
1. lag_1 (Yesterday's Price) -23.4% importance
2. MA_7 (7-day moving average) -18.7% importance
3. volatility(30-day) - 15.3 importance
4. MA_30 (30-day moving average) - 11.2% importance

## *Model Recommendations*
- Best Overall : Random Forest (95.4% R2, 4.8% MAPE)
- Fatest : Linear Regression (87.3% R2, instant predictions)
- Time Series : ARIMA (89.1 % R2, Captures trends)
- Production : Ensemble of Random Forest + ARIMA

### *Business Recommendations*
- Use for medium-term (7-30 day) investment decision
- Combine predictions with confidence intervals for risk management
- Retrain model monthly with new data
- Monitor model drift and recaliberate as needed
- use as one input among several (not sole decision factor)

# Business Applications

*investment Strategy*
- identity optimal entry / exit points
- portfolio rebalancing based on forecasts
- Risk-adjusted position sizing

*Risk Management*
- volatility assessment and monitoring
- Confidence interval-based stop losses
- Portfolio stress testing

*Market Analysis*
- Trend identification and validation
- Pattern recognition across timeframework
- Comparative analysis with market indics

#Performance Tracking
- Real-time forecast vs actual comparison
- Model accuracy monitoring
- Trading Strategy backtesting

# Future Enhancements

- Add Ethereum , Litecoin , and top 10 cryptocurrencies
- implements automated model retraining pipeline
- Add real-time Price feeds via API
- Create mobile-responsive dashboard
- Implements sentiment analysis
- Implements LSTM deep learning models
- Add automated trading Signal generation
- Building backtesting framework
- Expand to Stocks, forex ,Commodities
- Create portfolio optimization module
- Add risk management tools (Var, Cvar)
- Develop White-Label product

# *Author*

**Barkha Rani**
*Email :*  rbarkha131@gmail.com
*Linkedin :* www.linkedin.com/in/barkha-rani-70468a303




