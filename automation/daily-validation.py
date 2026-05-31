import pandas as pd

df = pd.read_csv("../data/experiment_results.csv")

print("===== DAILY VALIDATION =====\n")

# Missing values
missing = df.isnull().sum()

print("Missing Values")
print(missing)

print("\n-----------------\n")

# Duplicate sessions
duplicates = df["session_id"].duplicated().sum()

print("Duplicate Sessions")
print(duplicates)

print("\n-----------------\n")

# Traffic allocation
allocation = (
    df["variant"]
    .value_counts(normalize=True)
    * 100
)

print("Traffic Allocation (%)")
print(allocation.round(2))

print("\n-----------------\n")

# Conversion rates
conversion_rates = (
    df.groupby("variant")["conversion"]
    .mean()
    * 100
)

print("Conversion Rates (%)")
print(conversion_rates.round(2))

print("\nValidation Completed")
