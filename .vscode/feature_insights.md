# Feature Insights — Sales Dataset

## 1. Sales
- Represents: Transaction value
- Why useful: Directly reflects customer value
- Risk: Skewed by outliers
- Improvement: Log transform to reduce skew

## 2. City
- Represents: Geographic market
- Why useful: Different purchasing power and more to focus
- Risk: Small sample bias
- Improvement: One-hot encoding

## 3. Date
- Represents: Time of transaction
- Why useful: Trend and seasonality
- Risk: Raw date is not numeric
- Improvement: Extract day, month, weekday

## 4. Sales per City (derived)
- Represents: Market strength
- Why useful: Reduces noise from individual sales
- Improvement: Rolling averages

## 5. Transaction Frequency (future feature)
- Represents: Customer loyalty
- Why useful: Strong predictor of lifetime value
