# 🔁 End-to-End Experiment Walkthrough

This document explains the complete lifecycle of an A/B test in this system — from user interaction to final business decision.

---

## 1. Hypothesis Formation

A product hypothesis is defined:

> "Changing the homepage CTA will increase conversion rate by improving user intent clarity."

Stored in:
- docs/hypothesis.md
- docs/experiment-design.md

---

## 2. Experiment Setup

### Tracking Implementation:
- GTM configured for CTA click events
- GA4 event tracking enabled
- Experiment assignment logic deployed

File:
- gtm-experiment-setup.md
- tracking-plan.md

---

## 3. User Assignment Flow

Each user is assigned to a variant:


User visits page
→ user_id hashed
→ assigned to Variant A or B
→ stored in experiment_assignments table


Ensures:
- Sticky assignment
- Balanced traffic split
- No cross-contamination

---

## 4. Data Collection

User interactions are captured:

- Page views
- CTA clicks
- Add-to-cart events
- Purchases

Data flows into:
- GA4 → BigQuery raw events table

---

## 5. Data Transformation

BigQuery SQL pipelines process raw data:

- Sessionization
- Funnel mapping
- Revenue attribution
- Deduplication

Outputs:
- clean_events table
- funnel_metrics table
- experiment_metrics table

---

## 6. Quality & Validation Layer

Before analysis:

- Sample Ratio Mismatch (SRM) check
- Event parity validation
- Traffic split validation
- Anomaly detection (spikes/drops)

Ensures data reliability.

---

## 7. Statistical Analysis

Performed in Python notebooks:

- Conversion rate comparison
- Uplift calculation
- Confidence intervals
- Significance testing (p-value < 0.05)

Files:
- experiment-analysis.ipynb
- sample-size-calculation.ipynb
- sensitivity-analysis.ipynb

---

## 8. Dashboard Visualization

Results are visualized in Looker Studio:

- Executive KPI dashboard
- Funnel drop-off analysis
- Segment breakdown (device/channel)
- Variant comparison view

Files:
- looker-studio/dashboard-design.md
- calculated-fields.md
- data-model.md

---

## 9. CI/CD Monitoring

Automated system runs continuously:

- SQL validation (sqlfluff)
- Notebook execution checks
- Data quality validation scripts
- Slack alerts for anomalies

Workflow:

.github/workflows/experiment-validation.yml


---

## 10. Final Decision Making

All outputs are reviewed:

- Statistical significance
- Business impact
- Segment-level effects
- Risk considerations

Final output:

- recommendation-report.md
- decision-log.md
- rollout-plan.md

---

## 🧠 Summary

This system replicates a real-world experimentation pipeline used in modern data-driven product teams:

**Track → Assign → Collect → Transform → Validate → Analyze → Visualize → Decide**
