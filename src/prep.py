import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np



floodsOnlyFP = "../data/floodsOnlyFP.csv"
df = pd.read_csv(floodsOnlyFP)

df = df.dropna(axis=1, how='all')


features = ['Start Year', 'Latitude', 'Longitude', 'Magnitude']
targets = ['Start Year', 'Latitude', 'Longitude', 'Magnitude']

df = df.dropna(subset=features)
df = df[~df[features].isin([np.inf, -np.inf]).any(axis=1)]
df['Magnitude'] = np.clip(df['Magnitude'], 0, 10)

X_train, X_test = train_test_split(df[features], test_size=0.2, random_state=42)

models = {}
for target in targets:
    y_train = df.loc[X_train.index, target]
    y_test = df.loc[X_test.index, target]

    model = xgb.XGBRegressor(n_estimators=400, learning_rate=0.03)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"MSE for {target}: {mse}")

    models[target] = model

# Export as model_bundle
from types import SimpleNamespace
model_bundle = SimpleNamespace(**models)
