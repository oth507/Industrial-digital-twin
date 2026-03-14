
import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("industrial_energy_dataset.csv")

baseline_total = data["Baseline_kWh"].sum()

# Simple optimization logic
optimized = data["Baseline_kWh"] * 0.84
optimized_total = optimized.sum()

reduction = (baseline_total - optimized_total) / baseline_total * 100

print("Baseline Energy:", baseline_total, "kWh")
print("Optimized Energy:", optimized_total, "kWh")
print("Energy Reduction:", reduction, "%")
