from prep import df  # historical data
from prep import model_bundle
import numpy as np
import pandas as pd
#from prep import model_bundle


# Step 1: Count earthquakes per year historically
yearly_counts = df['Start Year'].value_counts().sort_index()
mean_per_year = int(yearly_counts.mean())  # or use median()


future_years = np.arange(2025, 2035)
samples_per_year = np.random.poisson(mean_per_year, size=len(future_years))


input_rows = []
for year, count in zip(future_years, samples_per_year):
    for _ in range(count):
        input_rows.append({
            'Start Year': year,
            'Latitude': np.random.uniform(df['Latitude'].min(), df['Latitude'].max()),
            'Longitude': np.random.uniform(df['Longitude'].min(), df['Longitude'].max()),
            'Magnitude': np.random.uniform(0, 10)
        })

future_df = pd.DataFrame(input_rows)

for target in ['Start Year', 'Latitude', 'Longitude', 'Magnitude']:
    input_features = ['Start Year', 'Latitude', 'Longitude', 'Magnitude']
    future_df[f'Predicted {target}'] = model_bundle.__dict__[target].predict(future_df[input_features])

future_df.to_csv('predicted_earthquakes.csv', index=False)

print(future_df.head())
