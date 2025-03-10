import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(df):
    """Train a predictive model on stock data."""
    df['Target'] = df['Adj Close'].shift(-1) > df['Adj Close']
    df.dropna(inplace=True)
    
    features = ['SMA_50', 'SMA_200', 'RSI_14', 'MACD']
    X = df[features]
    y = df['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))
    return model, accuracy

def predict_stock_movement(model, df):
    """Predict stock movement using the trained model."""
    features = ['SMA_50', 'SMA_200', 'RSI_14', 'MACD']
    df['Prediction'] = model.predict(df[features])
    return df['Prediction']
