import pandas as pd

print("=" * 50)
print("EXPERIMENT HEALTH MONITOR")
print("=" * 50)

df = pd.read_csv("../data/experiment_results.csv")

# Traffic Split

allocation = (
    df["variant"]
    .value_counts(normalize=True)
    * 100
)

control_pct = allocation.get(
    "control",
    0
)

variant_pct = allocation.get(
    "variant_b",
    0
)

print("\nTraffic Allocation")

print(f"Control : {control_pct:.2f}%")
print(f"Variant : {variant_pct:.2f}%")

if abs(control_pct - 50) > 5:
    print("ALERT: Traffic Split Imbalance")

# Conversion Rates

print("\nConversion Rates")

cr = (
    df.groupby("variant")
      ["conversion"]
      .mean()
      * 100
)

print(cr.round(2))

# Session Volume

print("\nTraffic Volume")

sessions = len(df)

print(f"Sessions: {sessions}")

if sessions < 5000:
    print("ALERT: Low Traffic Volume")

print("\nMonitoring Complete")
