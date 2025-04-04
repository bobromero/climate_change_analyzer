import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_processor import load_disaster


def prep(df):
    df = df.dropna(axis=1, how='all')
    features = ['Start Year', 'Latitude', 'Longitude', 'Total Deaths']
    targets = ['Latitude', 'Longitude', 'Total Deaths']
    df = df.dropna(subset=features)
    df = df[~df[features].isin([np.inf, -np.inf]).any(axis=1)]
    df["Total Deaths"] = np.clip(df["Total Deaths"], 0, 5000)
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
    #from types import SimpleNamespace
   # model_bundle = SimpleNamespace(**models)
    return models

def pred(df):
    future_years = np.arange(2025, 2035)
    future_months = np.tile(np.arange(1, 13), len(future_years))

    num_samples = len(future_years) * 12

    future_latitudes = np.random.uniform(-90, 90, num_samples)
    future_longitudes = np.random.uniform(-180, 180, num_samples)
    future_deaths = np.random.uniform(0, 5000, num_samples)


    future_df = pd.DataFrame({
        'Start Year': np.repeat(future_years, 12),
        'Latitude': future_latitudes,
        'Longitude': future_longitudes,
        'Total Deaths': future_deaths
    })
    models = prep(df)
    for target in ['Latitude', 'Longitude', 'Total Deaths']:
        input_features = ['Start Year', 'Latitude', 'Longitude', 'Total Deaths']
        future_df[f'{target}'] = models[target].predict(future_df[input_features])
    
    future_df["Total Deaths"] = future_df["Total Deaths"].astype(int)
    future_df["Start Year"] = future_df["Start Year"].astype(int)
    future_df = future_df.dropna(subset=input_features)
    return future_df


def vis(future_df, dis_type):
    plt.scatter(
        future_df["Longitude"],
        future_df["Latitude"],
        c=future_df["Total Deaths"],
        cmap="coolwarm",
        alpha=0.5,
    )
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title(f"Predicted {dis_type} Deaths (Next 10 Years)")
    plt.colorbar(label="Predicted Deaths")
    plt.show()


if __name__ == "__main__":
    disaster_type = "Earthquake"
    df = load_disaster(
        disaster_type,
        ["Start Year", "Start Month", "Latitude", "Longitude", "Total Deaths"],
    )
    print(f"running for {disaster_type}")
    #model = prep(df)
    future_df = pred(df)
    
    vis(future_df, disaster_type)
    
    csv_filename = f"../data/multipredictions.csv"
    future_df.to_csv(csv_filename, index=False)
    print(f"Predictions saved to {csv_filename}")

