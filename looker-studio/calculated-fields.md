# Looker Studio Calculated Fields

This file defines all derived metrics used in the dashboard.

---

## 1. Conversion Rate


Conversion Rate =
SUM(Conversions) / SUM(Sessions)


---

## 2. Add-to-Cart Rate


Add to Cart Rate =
SUM(Add_to_Cart) / SUM(Product_Views)


---

## 3. Purchase Uplift (Variant B vs A)


Uplift % =
(B Conversion Rate - A Conversion Rate)
/ A Conversion Rate


---

## 4. Bounce Rate


Bounce Rate =
1 - (Engaged Sessions / Total Sessions)


---

## 5. Statistical Significance Flag


IF p_value < 0.05 THEN "Significant" ELSE "Not Significant"


---

## 6. Revenue per User (RPU)


RPU =
SUM(Revenue) / COUNT(DISTINCT Users)


---

## Notes
- Metrics are calculated at session-level granularity unless specified.
- All filters are consistently applied across charts to avoid bias.
