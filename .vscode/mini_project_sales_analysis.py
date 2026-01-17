"""
MINI PROJECT: SALES DATA ANALYSIS

Objective:
Understand sales behavior, data quality issues, and ML readiness
using a real-world messy dataset.

This project demonstrates:
- Data cleaning
- Data understanding
- Visualization
- Feature thinking
- ML problem framing
"""
# =========================
# 1. DATA OVERVIEW
# =========================

"""
What is this data about?
- Transaction-level sales data
- Includes customer, city, sales amount, and date

Why does it matter?
- Helps understand revenue patterns
- Informs business and ML decisions
"""
# =========================
# 2. BUSINESS CONTEXT
# =========================

"""
Who would care about this data?
- Business owners
- Sales managers
- ML teams building demand prediction models

What decisions could it influence?
- Inventory planning
- Regional focus
- Sales forecasting
"""
# =========================
# 3. DATA QUALITY AUDIT
# =========================

"""
Issues found:
- Missing sales values
- Missing dates
- Negative sales values
- Potential outliers

Fixes applied:
- Dropped rows with critical missing values
- Removed invalid negative sales
- Used IQR to handle extreme outliers

Reasoning:
- ML models cannot learn from unreliable data
- Conservative cleaning preferred due to small dataset
"""
# =========================
# 4. KEY INSIGHTS
# =========================

"""
Insight 1:
Sales distribution is skewed with a few high-value transactions.
Implication:
Mean sales can be misleading; median is more reliable.
Decision:
Use median-based planning instead of averages.

Insight 2:
Certain cities contribute disproportionately to total sales.
Implication:
Geographic focus matters.
Decision:
Allocate resources by region.

Insight 3:
Sales over time show variability rather than stable growth.
Implication:
Forecasting will be uncertain.
Decision:
Combine ML predictions with human judgment.
"""
# =========================
# 5. FEATURE INSIGHTS
# =========================

"""
Promising features:
- Sales (target)
- City (geographic signal)
- Date (time patterns)

Noisy features:
- Individual transactions without aggregation

Potential transformations:
- Log-transform sales
- Aggregate sales by city/date
- Extract weekday/month from date
"""
# =========================
# 6. ML READINESS CHECK
# =========================

"""
Dataset size:
- Small (risk of overfitting)

Target variable:
- Sales (clear regression target)

Risks:
- Limited data
- No external factors (festivals, marketing)

Conclusion:
- Suitable for prototyping
- Not production-ready without more data
"""
