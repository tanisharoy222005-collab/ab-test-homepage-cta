# 📊 A/B Testing Analytics Engineering System

A production-style end-to-end experimentation analytics platform built using **BigQuery, SQL pipelines, Python analysis, Looker Studio dashboards, and CI/CD validation workflows**.

This project simulates how modern data teams run controlled experiments from **tracking → analysis → decision-making**.

---

# 🧠 System Overview

Event Tracking (GA4 / GTM)  
↓  
BigQuery Data Modeling  
↓  
Experiment Assignment Logic  
↓  
Data Quality & Validation Layer  
↓  
Statistical Analysis (Python)  
↓  
Looker Studio Dashboards  
↓  
CI/CD Monitoring & Alerts  
↓  
Business Decision Making  

---

# 🏗️ Architecture

architecture/
├── architecture-overview.md

Defines:
- Event ingestion flow
- Data transformation pipelines
- Experiment assignment logic
- BI reporting structure
- CI/CD validation system

---

# 📁 Repository Structure

## ⚙️ Automation Layer
automation/

- Daily validation scripts  
- Experiment monitoring system  
- Report generation automation  
- Slack alert integration  

---

## 🧱 BigQuery Data Layer
bigquery/

- Event extraction  
- Sessionization logic  
- Experiment schema design  

---

## 📊 SQL Analytics Layer
sql/

- Funnel analysis queries  
- Experiment metrics computation  
- Segment analysis logic  
- Variant assignment logic  

---

## 📉 Data Quality & Validation Layer
data-quality/
validation/

- Sample Ratio Mismatch (SRM) checks  
- Event parity validation  
- Traffic split validation  
- Anomaly detection logic  
- QA validation scripts  

---

## 📈 Analysis Layer (Python Notebooks)
notebooks/

- Experiment statistical analysis  
- Sample size calculation  
- Sensitivity analysis  
- Synthetic data generation  

---

## 📊 Looker Studio Layer
looker-studio/

- Dashboard design documentation  
- Calculated metrics definition  
- Data modeling structure  

---

## 📂 Experiment Documentation
docs/

- Hypothesis definition  
- Experiment design  
- Tracking plan  
- GTM setup  
- Risk assessment  
- Rollout plan  
- Statistical analysis report  
- Recommendation report  
- Post-launch monitoring  
- Retrospective analysis  

---

## 📊 Dashboard Layer
dashboard/

- KPI definitions  
- Executive summary  
- Metric calculations  
- Dashboard walkthrough  
- Requirements specification  

---

## 🧪 Data Layer
data/

- Experiment results dataset  
- CSV-based validation dataset  

---

# 📊 Key Capabilities Demonstrated

✔ Experimentation Engineering  
✔ Data Engineering (BigQuery)  
✔ Statistical Analysis (A/B testing)  
✔ Data Quality Engineering  
✔ Business Intelligence (Looker Studio)  
✔ Automation & CI/CD workflows  

---

# 📊 Key Metrics Tracked

- Conversion Rate  
- Add-to-Cart Rate  
- Revenue per User (RPU)  
- Bounce Rate  
- Uplift %  
- Statistical Significance (p-value)  

---

# 🧪 Experiment Lifecycle

1. Hypothesis Definition  
2. Experiment Design  
3. Tracking Setup (GTM / GA4)  
4. User Assignment (A/B split)  
5. Data Collection  
6. BigQuery Transformation  
7. Data Quality Validation  
8. Statistical Analysis  
9. Dashboard Reporting  
10. Business Decision + Rollout  

---

# 📉 Data Quality & Reliability

- Sample Ratio Mismatch detection  
- Event parity validation  
- Traffic split verification  
- Anomaly detection pipelines  
- CI-based validation workflows  

---

# 📊 Dashboards (Looker Studio)

- Executive KPI Summary  
- Funnel Drop-off Analysis  
- Segment Breakdown  
- Experiment Performance Comparison  
- Statistical Significance Tracking  

---

# ⚙️ CI/CD Validation Pipeline

validation/workflows/experiment-validation.yml

Validates:
- SQL syntax (sqlfluff)
- Notebook execution
- Data quality checks
- Experiment monitoring scripts

---

# 📌 Business Impact

- Faster product decision-making  
- Reliable A/B test validation  
- Reduced data inconsistencies  
- Automated monitoring & alerts  
- Scalable experimentation framework  

---

# 🧠 Key Learning Outcomes

- End-to-end experimentation system design  
- Analytics engineering best practices  
- BigQuery data modeling  
- Statistical testing in real-world scenarios  
- BI dashboard design (Looker Studio)  
- CI/CD for data workflows  

---

# 🧑‍💻 Author

This project simulates a real-world experimentation platform used in data-driven product organizations combining:

- Data Engineering  
- Analytics Engineering  
- Product Analytics  
- BI & Dashboarding  
- Automation & CI/CD  

---

# 🏁 Status

✔ Production-style analytics system  
✔ End-to-end experiment lifecycle  
✔ CI/CD validation integrated  
✔ SQL + Python + BI fully connected  
✔ Portfolio-ready architecture  
