import pandas as pd
import matplotlib.pyplot as plt

def analyze_natural_disasters(original_file, predicted_file, event_type="Disaster"):
    # Load datasets
    original_df = pd.read_csv(original_file)
    predicted_df = pd.read_csv(predicted_file)
    
    # Ensure necessary columns exist
    for df in [original_df]:
        if "Start Year" not in df or "Magnitude" not in df:
            raise ValueError("Datasets must contain 'Start Year' and 'Magnitude' columns.")
        
    for df in [predicted_df]:
        if "Start Year" not in df or "Predicted Magnitude" not in df:
            raise ValueError("Datasets must contain 'Start Year' and 'Magnitude' columns.")
        
    # Aggregate event counts and magnitude trends by year
    original_df["Year"] = original_df["Start Year"]
    predicted_df["Year"] = predicted_df["Start Year"]
    
    original_counts = original_df["Year"].value_counts().sort_index()
    predicted_counts = predicted_df["Year"].value_counts().sort_index()
    
    original_magnitude = original_df.groupby("Year")["Magnitude"].mean()
    predicted_magnitude = predicted_df.groupby("Year")["Predicted Magnitude"].mean()
    

    # Plot yearly frequency comparison
    plt.figure(figsize=(12, 6))
    plt.plot(original_counts.index, original_counts.values, marker="o", linestyle="-", color="b", label=f"Original {event_type} Count")
    plt.plot(predicted_counts.index, predicted_counts.values, marker="o", linestyle="--", color="orange", label=f"Predicted {event_type} Count")
    plt.xlabel("Year")
    plt.ylabel(f"Number of {event_type}s")
    plt.title(f"Yearly {event_type} Frequency: Original vs Predicted")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Plot magnitude trend comparison
    plt.figure(figsize=(12, 6))
    plt.plot(original_magnitude.index, original_magnitude.values, marker="o", linestyle="-", color="g", label=f"Original Avg {event_type} Magnitude")
    plt.plot(predicted_magnitude.index, predicted_magnitude.values, marker="o", linestyle="--", color="red", label=f"Predicted Avg {event_type} Magnitude")
    plt.xlabel("Year")
    plt.ylabel(f"Average {event_type} Magnitude")
    plt.title(f"Yearly {event_type} Magnitude Trend: Original vs Predicted")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return {
        "original_counts": original_counts,
        "predicted_counts": predicted_counts,
        "original_magnitude": original_magnitude,
        "predicted_magnitude": predicted_magnitude
    }


results = analyze_natural_disasters("../data/earthquakesOnlyFP.csv", "predicted_earthquakes.csv", event_type="Earthquake")
print(results)