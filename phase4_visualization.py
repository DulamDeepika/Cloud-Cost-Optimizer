import pandas as pd
import matplotlib.pyplot as plt

# Read Dataset
df = pd.read_csv("gcp_final_approved_dataset.csv")

print("=" * 50)
print("      DATA VISUALIZATION")
print("=" * 50)

# -----------------------------------------
# Chart 1 : Total Cost by Service
# -----------------------------------------

service_cost = df.groupby("Service Name")["Total Cost (INR)"].sum()

plt.figure(figsize=(12,6))
plt.bar(service_cost.index, service_cost.values)

plt.title("Total Cost by Cloud Service")
plt.xlabel("Cloud Service")
plt.ylabel("Total Cost (INR)")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

# -----------------------------------------
# Chart 2 : Total Cost by Region
# -----------------------------------------

region_cost = df.groupby("Region/Zone")["Total Cost (INR)"].sum()

plt.figure(figsize=(10,6))
plt.bar(region_cost.index, region_cost.values)

plt.title("Total Cost by Region")
plt.xlabel("Region")
plt.ylabel("Total Cost (INR)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# -----------------------------------------
# Chart 3 : Top 10 Expensive Resources
# -----------------------------------------

top10 = df.nlargest(10, "Total Cost (INR)")

plt.figure(figsize=(12,6))
plt.bar(top10["Resource ID"], top10["Total Cost (INR)"])

plt.title("Top 10 Expensive Resources")
plt.xlabel("Resource ID")
plt.ylabel("Total Cost (INR)")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

print("\nVisualization Completed Successfully")