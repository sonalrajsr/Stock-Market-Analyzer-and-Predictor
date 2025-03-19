
# Algorithmic Trading Project  
This project implements an **algorithmic trading strategy** using machine learning models to predict stock price movements and evaluate trading performance. It includes data collection, feature engineering, model building, backtesting, and optimization.


## 🚀 **1. Project Overview**
The goal of this project is to develop an **algorithmic trading strategy** using machine learning models. The project aims to:  
✅ Collect and preprocess stock market data  
✅ Engineer key technical indicators (SMA, RSI, MACD)  
✅ Build predictive models using Random Forest, XGBoost, and LSTM  
✅ Backtest the strategy and evaluate performance  
✅ Optimize the strategy using hyperparameter tuning and risk management  

---

## 🌐 **2. Data Source**
The historical stock data is obtained from the **Yahoo Finance API** using the `yfinance` Python library.  
- **Ticker:** AAPL (Apple Inc.)  
- **Timeframe:** 2010 to 2023  
- **Data Fields:**  
  - `Open` – Opening price  
  - `High` – Highest price  
  - `Low` – Lowest price  
  - `Close` – Closing price  
  - `Adj Close` – Adjusted closing price  
  - `Volume` – Number of shares traded  

---

## 📊 **3. Technical Indicators**
To enhance model performance, we compute several widely-used technical indicators:

### ✅ **1. Moving Average (SMA)**
- Simple Moving Average over 50 and 200 days:  
\[
SMA_t = \frac{P_{t} + P_{t-1} + ... + P_{t-n}}{n}
\]

### ✅ **2. Relative Strength Index (RSI)**
- Measures the magnitude of price changes to identify overbought/oversold conditions:  
\[
RSI = 100 - \frac{100}{1 + RS}
\]
where  
\[
RS = \frac{\text{Average Gain over n periods}}{\text{Average Loss over n periods}}
\]

### ✅ **3. Moving Average Convergence Divergence (MACD)**
- Measures the relationship between two moving averages:  
\[
MACD = EMA_{12} - EMA_{26}
\]
Signal Line:  
\[
Signal = EMA_9(MACD)
\]

---

## 🤖 **4. Models Used**
### ✅ **1. Random Forest**
- Ensemble-based classifier that works on decision trees.
- Parameters tuned using **GridSearchCV**.  
- Works well with noisy data and handles high-dimensional datasets.

### ✅ **2. XGBoost**
- Gradient boosting-based classifier.
- Handles missing data and is computationally efficient.
- Parameters tuned using **RandomizedSearchCV**.

### ✅ **3. LSTM (Long Short-Term Memory)**
- A type of Recurrent Neural Network (RNN).
- Captures sequential dependencies in time-series data.
- Trained with a **lookback period** of 50 days.

---

## 🏆 **5. Strategy and Backtesting**
### ✅ **Trading Strategy**
1. **Buy** when the model predicts price will go up.  
2. **Sell** when the model predicts price will go down.  

### ✅ **Risk Management**
- **Stop-Loss:** Exit the trade if the price drops by 2%.  
- **Take-Profit:** Exit the trade if the price increases by 4%.  
- **Transaction Cost:** 0.1% applied to every trade.  

---

### ✅ **Backtesting**
- Backtest performed on historical data.
- Metrics Calculated:
  - **Cumulative Return** – Total strategy performance.
  - **Sharpe Ratio** – Measures risk-adjusted return.
  - **Max Drawdown** – Measures peak-to-trough loss.  

---

## 🎯 **6. Optimization and Risk Management**
### ✅ **Hyperparameter Tuning**
1. **Random Forest:**  
   - `n_estimators`: 50, 100, 200  
   - `max_depth`: None, 10, 20  
   - `min_samples_split`: 2, 5, 10  
   - `min_samples_leaf`: 1, 2, 4  

2. **XGBoost:**  
   - `learning_rate`: 0.01, 0.1, 0.2  
   - `n_estimators`: 50, 100, 200  
   - `max_depth`: 3, 5, 7  
   - `subsample`: 0.8, 1.0  

---

## 📏 **7. Evaluation Metrics**
### ✅ **Classification Models**  
- **Accuracy**  
- **Precision**  
- **Recall**  
- **F1 Score**  
- **Confusion Matrix**  
- **ROC-AUC Curve**  

### ✅ **Regression Models**  
- **Mean Absolute Error (MAE)**  
- **Mean Squared Error (MSE)**  
- **R2 Score**  

---

## ⚙️ **8. Installation**
### ✅ **Setup Environment**
```bash
pip install -r requirements.txt
```

### ✅ **Requirements File**
```
numpy
pandas
matplotlib
seaborn
yfinance
scikit-learn
xgboost
tensorflow
streamlit
```

---

## 🚦 **9. Usage**
### ✅ **Run Streamlit App**
```bash
streamlit run app.py
```

### ✅ **Run Backtesting**
```python
python backtest.py
```

---

## 📊 **10. Results and Insights**
### ✅ **Best Model:**  
- **XGBoost** model provided the best accuracy and Sharpe ratio.  

### ✅ **Performance:**  
| Model | Accuracy | Sharpe Ratio | Max Drawdown | AUC |  
|-------|----------|--------------|--------------|-----|  
| Random Forest | 68% | 1.45 | -12% | 0.72 |  
| XGBoost | 72% | 1.65 | -10% | 0.78 |  
| LSTM | 69% | 1.50 | -11% | N/A |  

---

## 🚀 **11. Future Improvements**
✅ **Add More Features:**  
- Include market sentiment, volume-weighted averages, and more.  
✅ **Use More Complex Models:**  
- Try Transformer-based models for better sequence prediction.  
✅ **Refine Strategy:**  
- Implement dynamic stop-loss and trailing stop-loss.  
✅ **Multi-Asset Portfolio:**  
- Extend strategy to trade across multiple assets.  

---