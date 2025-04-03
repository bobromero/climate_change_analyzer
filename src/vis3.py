import geopandas as gpd
import matplotlib.pyplot as plt
from pred import future_df  # use the generated predictions directly

# Load base map
world = gpd.read_file(r"C:\Users\isabe\Desktop\110m_cultural\ne_110m_admin_0_countries.shp")

# Load fault lines
faults = gpd.read_file(r"C:\Users\isabe\Desktop\gem-global-active-faults-2019.0\GEMScienceTools-gem-global-active-faults-03ad3ff\shapefile")

# Plot
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(ax=ax, color='lightgray', edgecolor='black')
faults.plot(ax=ax, color='red', linewidth=0.8, label='Fault Lines')

scatter = ax.scatter(
    future_df['Predicted Longitude'], future_df['Predicted Latitude'],
    c=future_df['Predicted Magnitude'], cmap='coolwarm',
    alpha=0.6, s=40, edgecolor='k', label='Predicted Earthquakes'
)

plt.colorbar(scatter, label='Predicted Magnitude')
plt.legend()
plt.title("Predicted Earthquakes with Fault Lines (2025–2034)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()
