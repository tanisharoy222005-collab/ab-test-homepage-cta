# 🏗️ Experiment Analytics Architecture Overview

This document explains the full data flow of the A/B testing analytics system.

---

## 1. Event Collection Layer (GTM + GA4)

### Flow
User Interaction → GTM Tags → GA4 Events → BigQuery Export

### What happens here:
- Page views, clicks, purchases are tracked via GTM
- GA4 collects and standardizes event schema
- Events are exported to BigQuery raw tables

### Output:
- Raw event stream
- User-level behavioral logs
2. BigQuery Transformation Layer
## 2. BigQuery Transformation Layer

### Flow
Raw GA4 Events → SQL Models → Clean Analytics Tables

### Key transformations:

- Sessionization of user events
- Funnel stage mapping
- Device + channel enrichment
- Bot filtering
- Deduplication logic

### Key SQL modules:
- sessionization.sql
- conversion_funnel.sql
- experiment_metrics.sql

### Output:
- Clean events table
- Session-level dataset
- Funnel analytics tables
3. Experiment Assignment Logic
## 3. Experiment Assignment Logic

### Flow
User ID → Hashing Function → Variant Assignment (A/B)

### Logic:
- Deterministic assignment using user_id hash
- Sticky assignment across sessions
- Balanced traffic split validation

### Validation:
- Sample Ratio Mismatch (SRM) checks
- Traffic split validation SQL
- assignment table in BigQuery

### Output:
- experiment_assignments table
4. Dashboard Layer (Looker Studio)
## 4. Dashboard Layer (Looker Studio)

### Flow
BigQuery Tables → Looker Studio Data Source → Dashboards

### Components:
- Funnel analysis dashboard
- Executive KPI summary
- Segment breakdown (device/channel/user type)
- Experiment performance tracking

### Key Metrics:
- Conversion Rate
- Uplift %
- Bounce Rate
- Revenue per User

### Output:
- Live BI dashboards for stakeholders
5. CI Validation Layer (Data Quality + Automation)
## 5. CI Validation Layer

### Flow
Git Push → GitHub Actions → Validation Scripts → Alerts

### Checks performed:

#### SQL Validation
- Syntax checks (sqlfluff)
- Query correctness verification

#### Notebook Execution
- Ensures reproducibility
- Runs analysis.ipynb + sample size notebooks

#### Data Quality Checks
- Sample Ratio Mismatch detection
- Event parity validation
- Traffic split validation
- Anomaly detection

### Automation:
- Daily validation script runs
- Slack alerts on failures
- Experiment monitor triggers

### Output:
- CI status reports
- Slack notifications
- Validation logs
