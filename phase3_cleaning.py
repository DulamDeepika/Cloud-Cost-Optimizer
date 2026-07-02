import pandas as pd

# Read Dataset
df = pd.read_csv("gcp_final_approved_dataset.csv")

print("=" * 50)
print("         DATA CLEANING")
print("=" * 50)

# 1. Check Missing Values
print("\n1. Missing Values")
print(df.isnull().sum())

# 2. Check Duplicate Records
print("\n2. Duplicate Records")
print(df.duplicated().sum())

# 3. Remove Duplicate Records
df = df.drop_duplicates()

print("\n3. Shape After Removing Duplicates")
print(df.shape)

# 4. Check Data Types
print("\n4. Data Types")
print(df.dtypes)

print("\nData Cleaning Completed Successfully!")