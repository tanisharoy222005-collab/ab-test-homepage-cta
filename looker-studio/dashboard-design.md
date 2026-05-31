# Looker Studio Dashboard Design

## Overview
This dashboard was designed to monitor A/B test performance, funnel behavior, and conversion impact across variants.

It is structured for three audiences:
- Product Managers → decision-making
- Growth/Marketing → campaign optimization
- Analysts → deep-dive exploration

---

## Dashboard Layout

### 1. Executive Summary (Top Section)
- Overall conversion rate
- Uplift between Variant A vs Variant B
- Statistical significance indicator (p-value + confidence interval)

### 2. Funnel Analysis
- Sessions → Product View → Add to Cart → Purchase
- Drop-off rate per step
- Variant comparison toggle

### 3. Experiment Performance
- Conversion rate over time
- Rolling 7-day average
- Traffic split validation

### 4. Segment Breakdown
- Device (mobile/desktop)
- Channel (organic/paid/email)
- New vs returning users

---

## Design Principles
- Minimal visual noise
- KPI-first layout
- Consistent time window filtering
- Always highlight statistical significance

---

## Interaction Features
- Date range selector
- Variant filter (A/B/C)
- Segment drill-down
