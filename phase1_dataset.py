import pandas as pd

# Read Dataset
df = pd.read_csv("gcp_final_approved_dataset.csv")

print("========== CLOUD BILLING DATASET ==========\n")

# First 5 rows
print(df.head())

print("\n==============================")

# Shape
print("Shape of Dataset")
print(df.shape)

print("\n==============================")

# Column Names
print("Column Names")
print(df.columns)

print("\n==============================")

# Information
print("Dataset Information")
print(df.info())

print("\n==============================")

# Summary Statistics
print("Summary Statistics")
print(df.describe())