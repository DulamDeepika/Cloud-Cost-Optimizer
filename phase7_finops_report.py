# ==========================================
# PHASE 7 : FINOPS REPORT GENERATOR
# ==========================================

import pandas as pd

# Read Dataset
df = pd.read_csv("gcp_final_approved_dataset.csv")

print("=" * 70)
print("           FINOPS CLOUD COST REPORT")
print("=" * 70)

# Total Resources
total_resources = len(df)

# Total Cloud Cost
total_cost = df["Total Cost (INR)"].sum()

# Average CPU
avg_cpu = df["CPU Utilization (%)"].mean()

# Average Memory
avg_memory = df["Memory Utilization (%)"].mean()

# High Utilization Resources
high_utilization = df[
    (df["CPU Utilization (%)"] > 80) |
    (df["Memory Utilization (%)"] > 80)
]

# Under Utilized Resources
under_utilization = df[
    (df["CPU Utilization (%)"] < 20) &
    (df["Memory Utilization (%)"] < 20)
]

# Estimated Savings
estimated_savings = under_utilization["Total Cost (INR)"].sum() * 0.50

# Print Report
print("\nTotal Resources          :", total_resources)
print("Total Cloud Cost         : ₹", round(total_cost, 2))
print("Average CPU Utilization  :", round(avg_cpu, 2), "%")
print("Average Memory Usage     :", round(avg_memory, 2), "%")
print("High Utilization Count   :", len(high_utilization))
print("Idle/Under Utilized      :", len(under_utilization))
print("Estimated Savings        : ₹", round(estimated_savings, 2))

print("\nTop 5 Costly Resources")
print("-" * 70)

top5 = df.nlargest(5, "Total Cost (INR)")

print(top5[
    [
        "Resource ID",
        "Service Name",
        "Region/Zone",
        "Total Cost (INR)"
    ]
])

# Save Report to CSV
report = pd.DataFrame({
    "Metric": [
        "Total Resources",
        "Total Cloud Cost",
        "Average CPU Utilization",
        "Average Memory Utilization",
        "High Utilization Resources",
        "Under Utilized Resources",
        "Estimated Savings"
    ],
    "Value": [
        total_resources,
        round(total_cost, 2),
        round(avg_cpu, 2),
        round(avg_memory, 2),
        len(high_utilization),
        len(under_utilization),
        round(estimated_savings, 2)
    ]
})

report.to_csv("FinOps_Report.csv", index=False)

print("\nReport Generated Successfully")
print("File Saved : FinOps_Report.csv")

print("=" * 70)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 70)