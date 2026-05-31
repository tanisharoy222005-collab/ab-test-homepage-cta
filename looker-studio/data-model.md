# Looker Studio Data Model

## Data Sources

The dashboard is built on a blended dataset from:

- GA4 Events Export
- Google Ads campaign data
- Experiment assignment table
- Transactional purchase data

---

## Core Tables

### 1. events
- user_id
- session_id
- event_name
- timestamp
- device_category

---

### 2. experiment_assignments
- user_id
- experiment_id
- variant (A / B)
- assignment_timestamp

---

### 3. transactions
- transaction_id
- user_id
- revenue
- purchase_timestamp

---

## Data Relationships


events.user_id → experiment_assignments.user_id
transactions.user_id → experiment_assignments.user_id


---

## Data Blending Logic

- Join type: LEFT JOIN (primary = events)
- Grain: session-level analysis
- Deduplication on (user_id + session_id)

---

## Key Assumptions

- Variant assignment is sticky per user across sessions
- Cross-device identity resolved via user_id
- Bot traffic filtered before ingestion layer
