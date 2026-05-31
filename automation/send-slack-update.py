from datetime import datetime

message = f"""
EXPERIMENT STATUS UPDATE

Date:
{datetime.now().strftime('%Y-%m-%d')}

Experiment:
Homepage CTA Optimization

Current Status:
Running

Traffic Split:
50 / 50

Observed Lift:
+12.2%

Recommendation:
Continue monitoring until experiment completion.
"""

print("=" * 50)
print("SIMULATED SLACK MESSAGE")
print("=" * 50)

print(message)

print("Slack notification sent.")
