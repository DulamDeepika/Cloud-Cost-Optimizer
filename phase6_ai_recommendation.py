import pandas as pd

# Read dataset
df = pd.read_csv("gcp_final_approved_dataset.csv")

print("=" * 60)
print("PHASE 6 : AI RECOMMENDATION ENGINE")
print("=" * 60)

total_savings = 0

for index, row in df.iterrows():

    cpu = row["CPU Utilization (%)"]
    memory = row["Memory Utilization (%)"]
    cost = row["Total Cost (INR)"]

    print("\n-----------------------------------")
    print("Resource ID :", row["Resource ID"])
    print("Service Name :", row["Service Name"])
    print("Region :", row["Region/Zone"])

    if cpu < 20 and memory < 20:
        savings = cost * 0.50
        total_savings += savings

        print("Recommendation : Stop or Resize Resource")
        print("Estimated Savings : ₹", round(savings, 2))

    elif cpu > 80 or memory > 80:
        print("Recommendation : Upgrade Resource")

    else:
        print("Recommendation : Running Efficiently")

print("\n========================================")
print("Total Estimated Savings : ₹", round(total_savings, 2))
print("========================================")