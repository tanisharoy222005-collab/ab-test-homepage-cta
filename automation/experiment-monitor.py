import pandas as pd

df = pd.read_csv("../data/experiment_results.csv")

print("===== EXPERIMENT MONITOR =====\n")

# Traffic split monitoring
allocation = (
    df["variant"]
    .value_counts(normalize=True)
)

control_pct = allocation["control"] * 100
variant_pct = allocation["variant_b"] * 100

print(f"Control: {control_pct:.2f}%")
print(f"Variant B: {variant_pct:.2f}%")

if abs(control_pct - 50) > 5:
    print("WARNING: Traffic imbalance detected")

print("\n-----------------\n")

# Conversion monitoring

cr = (
    df.groupby("variant")["conversion"]
    .mean()
    * 100
)

print("Conversion Rates")

for variant, value in cr.items():
    print(f"{variant}: {value:.2f}%")

print("\n-----------------\n")

# Daily volume monitoring

if len(df) < 5000:
    print("WARNING: Traffic volume lower than expected")
else:
    print("Traffic volume within expected range")

print("\nMonitoring Complete")
