import pandas as pd

# Read the dataset
df = pd.read_csv("gcp_final_approved_dataset.csv")

print("========== CLOUD COST ANALYSIS ==========\n")

# 1. Total Cloud Cost
print("1. Total Cloud Cost (INR)")
print(df["Total Cost (INR)"].sum())

print("\n----------------------------------")

# 2. Average Cloud Cost
print("2. Average Cloud Cost (INR)")
print(df["Total Cost (INR)"].mean())

print("\n----------------------------------")

# 3. Highest Cost Resource
highest = df.loc[df["Total Cost (INR)"].idxmax()]

print("3. Highest Cost Resource")
print(highest)

print("\n----------------------------------")

# 4. Lowest Cost Resource
lowest = df.loc[df["Total Cost (INR)"].idxmin()]

print("4. Lowest Cost Resource")
print(lowest)

print("\n----------------------------------")

# 5. Total Cost by Service
print("5. Total Cost by Service")
service_cost = df.groupby("Service Name")["Total Cost (INR)"].sum()
print(service_cost)

print("\n----------------------------------")

# 6. Total Cost by Region
print("6. Total Cost by Region")
region_cost = df.groupby("Region/Zone")["Total Cost (INR)"].sum()
print(region_cost)

print("\n----------------------------------")

# 7. Top 10 Most Expensive Resources

top10 = df.nlargest(10, "Total Cost (INR)")

print("Top 10 Most Expensive Resources")
print(top10[["Resource ID", "Service Name", "Region/Zone", "Total Cost (INR)"]])