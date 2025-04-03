import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from scipy.stats import zscore
import matplotlib.pyplot as plt
from data_processor import load_disaster

# Function to perform ADF test (checks for stationarity by testing for unit root)
def adf_test(series):
    if len(series.unique()) == 1:  # Check if the series is constant
        print("Series is constant. Skipping ADF test.")
        return None, None  # Returning None values to indicate test was skipped
    result = adfuller(series)
    return result[0], result[1]  # ADF Statistic and p-value

# Load data
disaster_type = "Earthquake"
original_df = load_disaster(
    disaster_type,
    ["Start Year", "Start Month", "Latitude", "Longitude", "Total Deaths"],
)
original_df = original_df.dropna()
predicted_df = pd.read_csv("../data/predictions.csv")

# Ensure necessary columns exist
for df in [original_df, predicted_df]:
    if "Start Year" not in df or "Total Deaths" not in df:
        raise ValueError("Datasets must contain 'Start Year' and 'Total Deaths' columns.")

# Aggregate deaths by year
original_deaths= original_df.groupby("Start Year")["Total Deaths"].mean()
predicted_deaths = predicted_df.groupby("Start Year")["Total Deaths"].mean()

# Perform ADF test on original data if not constant
adf_stat, adf_p = adf_test(original_deaths)
is_stationary_original = adf_p is not None and adf_p < 0.05  # Check stationarity only if test ran

# If original data is non-stationary, apply differencing
if not is_stationary_original and adf_p is not None:
    original_diff = original_deaths.diff().dropna()  # First difference to make it stationary
    adf_stat_diff, adf_p_diff = adf_test(original_diff)
    is_stationary_diff_original = adf_p_diff is not None and adf_p_diff < 0.05

# Perform ADF test on predicted data if not constant
adf_stat_predicted, adf_p_predicted = adf_test(predicted_deaths)
is_stationary_predicted = adf_p_predicted is not None and adf_p_predicted < 0.05

# If predicted data is non-stationary, apply differencing
if not is_stationary_predicted and adf_p_predicted is not None:
    predicted_diff = predicted_deaths.diff().dropna()
    adf_stat_diff_predicted, adf_p_diff_predicted = adf_test(predicted_diff)
    is_stationary_diff_predicted = adf_p_diff_predicted is not None and adf_p_diff_predicted < 0.05

# Anomaly detection using Z-score for original data
z_scores_original = zscore(original_deaths.fillna(0))
anomalies_zscore_original = original_deaths[np.abs(z_scores_original) > 2.5]

# Anomaly detection using IQR for original data
Q1_original = original_deaths.quantile(0.25)
Q3_original = original_deaths.quantile(0.75)
IQR_original = Q3_original - Q1_original
anomalies_iqr_original = original_deaths[
    (original_deaths < (Q1_original - 1.5 * IQR_original)) |
    (original_deaths > (Q3_original + 1.5 * IQR_original))
]

# Combine anomalies from both methods for original data
all_anomalies_original = pd.concat([anomalies_zscore_original, anomalies_iqr_original]).drop_duplicates()

# Anomaly detection using Z-score for predicted data
z_scores_predicted = zscore(predicted_deaths.fillna(0))
anomalies_zscore_predicted = predicted_deaths[np.abs(z_scores_predicted) > 2.5]

# Anomaly detection using IQR for predicted data
Q1_predicted = predicted_deaths.quantile(0.25)
Q3_predicted = predicted_deaths.quantile(0.75)
IQR_predicted = Q3_predicted - Q1_predicted
anomalies_iqr_predicted = predicted_deaths[
    (predicted_deaths < (Q1_predicted - 1.5 * IQR_predicted)) |
    (predicted_deaths > (Q3_predicted + 1.5 * IQR_predicted))
]

# Combine anomalies from both methods for predicted data
all_anomalies_predicted = pd.concat([anomalies_zscore_predicted, anomalies_iqr_predicted]).drop_duplicates()

# Combine anomalies from original and predicted data
all_anomalies = pd.concat([all_anomalies_original, all_anomalies_predicted]).drop_duplicates()

# Save only anomalies to a CSV file
all_anomalies.to_csv("../data/anomalies.csv", header=["Total Deaths"])

print("Anomalies saved to ../data/anomalies.csv")
