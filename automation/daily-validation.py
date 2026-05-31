import pandas as pd

print("=" * 50)
print("DAILY DATA QUALITY VALIDATION")
print("=" * 50)

df = pd.read_csv("../data/experiment_results.csv")

# Missing Values

print("\n[1] Missing Values")

missing = df.isnull().sum()

print(missing)

# Duplicate Sessions

print("\n[2] Duplicate Sessions")

duplicates = df["session_id"].duplicated().sum()

print(f"Duplicate Sessions: {duplicates}")

# Variant Allocation

print("\n[3] Traffic Allocation")

allocation = (
    df["variant"]
    .value_counts(normalize=True)
    * 100
)

print(allocation.round(2))

# Event Completeness

print("\n[4] Conversion Tracking")

conversion_count = df["conversion"].sum()

print(
    f"Total Conversions: {conversion_count}"
)

print("\nValidation Complete")
