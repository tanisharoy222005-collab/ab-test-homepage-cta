import pandas as pd
from datetime import datetime

df = pd.read_csv(
    "../data/experiment_results.csv"
)

summary = (
    df.groupby("variant")
      .agg(
          sessions=("session_id", "count"),
          conversions=("conversion", "sum")
      )
)

summary["conversion_rate"] = (
    summary["conversions"]
    /
    summary["sessions"]
    * 100
)

control_cr = summary.loc[
    "control",
    "conversion_rate"
]

variant_cr = summary.loc[
    "variant_b",
    "conversion_rate"
]

lift = (
    (variant_cr - control_cr)
    /
    control_cr
) * 100

report = f"""
EXPERIMENT SUMMARY REPORT

Generated:
{datetime.now()}

Control Conversion Rate:
{control_cr:.2f}%

Variant Conversion Rate:
{variant_cr:.2f}%

Relative Lift:
{lift:.2f}%

Recommendation:
Deploy Variant B if statistical significance criteria are met.
"""

print(report)

with open(
    "../docs/automated-experiment-summary.txt",
    "w"
) as file:
    file.write(report)

print("Report Saved")
