# DAY 2 - DATA HANDLING

# 1. LISTS
customers = ["Amit", "Neha", "Rahul"]

print(customers)
print(customers[0])
print(customers[-1])
# Modify list
customers.append("Priya")
customers[1] = "Neha Sharma"

print(customers)
# 2. TUPLES (fixed data)
months = ("Jan", "Feb", "Mar")

print(months)
print(months[0])
print(months[-1])
# 3. DICTIONARIES (single record / row)
customer = {
    "id": 101,
    "name": "Neha",
    "age": 41,
    "city": "Indore",
    "spent": 12000
}

print(customer)
print(customer["name"])
print(customer["spent"])
# Modify dictionary
customer["spent"] = 15000
customer["membership"] = "Gold"

print(customer)
# 4. LIST OF DICTIONARIES (table)
customers_data = [
    {"name": "Amit", "age": 35, "spent": 8000},
    {"name": "Neha", "age": 41, "spent": 12000},
    {"name": "Rahul", "age": 29, "spent": 5000}
]

for c in customers_data:
    print(c["name"], c["spent"])
# 4. LIST OF DICTIONARIES (table thinking)
customers_data = [
    {"name": "Amit", "age": 35, "spent": 8000},
    {"name": "Neha", "age": 41, "spent": 12000},
    {"name": "Rahul", "age": 29, "spent": 5000}
]

for c in customers_data:
    print(c["name"], c["spent"])
# 5. NUMPY ARRAYS
import numpy as np
sales = np.array([8000, 12000, 5000, 15000])

print(sales)
print("Max:", sales.max())
print("Min:", sales.min())
print("Mean:", sales.mean())
print("Total:", sales.sum())
# 6. PANDAS DATAFRAME
import pandas as pd
data = {
    "Name": ["Amit", "Neha", "Rahul"],
    "Age": [35, 41, 29],
    "Spent": [8000, 12000, 5000]
}

df = pd.DataFrame(data)
print(df)
print("\nHEAD:")
print(df.head())

print("\nINFO:")
print(df.info())

print("\nDESCRIBE:")
print(df.describe())
# 7. LOAD REAL CSV
df_sales = pd.read_csv("sales_data.csv")

print(df_sales)
# Select single column
print(df_sales["Sales"])

# Select multiple columns
print(df_sales[["Customer", "Sales"]])
# Filter rows: high sales
high_sales = df_sales[df_sales["Sales"] > 10000]
print(high_sales)
# Filter rows: city = Indore
indore_sales = df_sales[df_sales["City"] == "Indore"]
print(indore_sales)
# Sort by sales (descending)
sorted_sales = df_sales.sort_values(by="Sales", ascending=False)
print(sorted_sales)
# Sort by city then sales
sorted_city_sales = df_sales.sort_values(by=["City", "Sales"])
print(sorted_city_sales)
# Aggregations
print("Total Sales:", df_sales["Sales"].sum())
print("Average Sales:", df_sales["Sales"].mean())
print("Max Sale:", df_sales["Sales"].max())
# Group by city
city_sales = df_sales.groupby("City")["Sales"].sum()
print(city_sales)
# DATA CLEANING

# Clean column names
df_sales.columns = df_sales.columns.str.lower().str.strip()
print(df_sales.columns)
print(df_sales.info())
# Convert date to datetime
df_sales["date"] = pd.to_datetime(df_sales["date"], errors="coerce")

print(df_sales.info())
print(df_sales.isnull().sum())
df_sales_clean = df_sales.dropna()
print(df_sales_clean)
df_sales_clean = df_sales_clean[df_sales_clean["sales"] >= 0]
print(df_sales_clean)
df_sales = pd.read_csv("sales_data.csv")

df_sales.columns = df_sales.columns.str.lower().str.strip()
df_sales["date"] = pd.to_datetime(df_sales["date"], errors="coerce")
# Use cleaned version for analysis
df = df_sales.copy()
# Missing values analysis
print("Missing values per column:")
print(df.isnull().sum())
# Missing values break AI because models cannot learn from unknown inputs
print("Sales statistics:")
print(df["sales"].describe())
# Detect potential outliers
high_outliers = df[df["sales"] > df["sales"].mean() + 2 * df["sales"].std()]
low_outliers = df[df["sales"] < df["sales"].mean() - 2 * df["sales"].std()]

print("High outliers:")
print(high_outliers)

print("Low outliers:")
print(low_outliers)
# Basic statistics
mean_sales = df["sales"].mean()
median_sales = df["sales"].median()
std_sales = df["sales"].std()

print("Mean sales:", mean_sales)
print("Median sales:", median_sales)
print("Standard deviation:", std_sales)
# Why bad data breaks AI:
# 1. Missing values create biased learning
# 2. Outliers distort model predictions
# 3. Wrong data types confuse algorithms
# 4. Models amplify data errors, not fix them
# Final clean dataset
df_final = df.dropna()
df_final = df_final[df_final["sales"] >= 0]

print("Final cleaned dataset:")
print(df_final)
# Missing data classification:
# Sales missing for Amit (Bhopal) → likely MAR (depends on city / reporting)
# Date missing for Neha → likely MCAR (random entry issue)
# ----- Missing value handling comparison -----

# Option 1: Drop missing values
df_drop = df.dropna()

# Option 2: Fill missing sales with median
df_fill = df.copy()
df_fill["sales"] = df_fill["sales"].fillna(df_fill["sales"].median())

print("Drop version row count:", len(df_drop))
print("Fill version row count:", len(df_fill))
# ----- Outlier detection using IQR -----

Q1 = df["sales"].quantile(0.25)
Q3 = df["sales"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)

outliers_iqr = df[(df["sales"] < lower_bound) | (df["sales"] > upper_bound)]
print("IQR Outliers:")
print(outliers_iqr)
# ----- FINAL TRUSTED DATASET -----

df_final = df.copy()
df_final = df_final.dropna()
df_final = df_final[df_final["sales"] >= 0]
df_final = df_final[
    (df_final["sales"] >= lower_bound) &
    (df_final["sales"] <= upper_bound)
]

print("FINAL DATASET FOR AI / ANALYSIS")
print(df_final)
