# ==========================================
# PHASE 5 : MACHINE LEARNING
# Improved Cloud Cost Prediction
# ==========================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


print("=" * 60)
print("PHASE 5 : MACHINE LEARNING - CLOUD COST PREDICTION")
print("=" * 60)

# Load dataset
df = pd.read_csv("gcp_final_approved_dataset.csv")

# Use real cost-driving features
X = df[
    [
        "Usage Quantity",
        "Cost per Quantity ($)",
        "Service Name",
        "Region/Zone",
        "CPU Utilization (%)",
        "Memory Utilization (%)"
    ]
]

# Target
y = df["Total Cost (INR)"]

print("\nInput Features :", list(X.columns))
print("Target Column : Total Cost (INR)")

# Numerical and categorical columns
numerical_features = [
    "Usage Quantity",
    "Cost per Quantity ($)",
    "CPU Utilization (%)",
    "Memory Utilization (%)"
]

categorical_features = [
    "Service Name",
    "Region/Zone"
]

# Convert text columns into numbers
preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numerical_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Build ML pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regression", LinearRegression())
    ]
)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Test prediction
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)
print("Mean Absolute Error (MAE) :", round(mae, 2))
print("Mean Squared Error (MSE)  :", round(mse, 2))
print("R² Score                  :", round(r2, 4))
print("Model Performance (R² %)  :", round(r2 * 100, 2), "%")

# New prediction
print("\n" + "=" * 60)
print("PREDICT NEW RESOURCE COST")
print("=" * 60)

usage_quantity = float(input("Enter Usage Quantity : "))
cost_per_quantity = float(input("Enter Cost per Quantity ($) : "))
service_name = input("Enter Service Name (example: BigQuery) : ")
region_zone = input("Enter Region/Zone (example: us-central1) : ")
cpu_utilization = float(input("Enter CPU Utilization (%) : "))
memory_utilization = float(input("Enter Memory Utilization (%) : "))

new_resource = pd.DataFrame(
    [[
        usage_quantity,
        cost_per_quantity,
        service_name,
        region_zone,
        cpu_utilization,
        memory_utilization
    ]],
    columns=[
        "Usage Quantity",
        "Cost per Quantity ($)",
        "Service Name",
        "Region/Zone",
        "CPU Utilization (%)",
        "Memory Utilization (%)"
    ]
)

predicted_cost = model.predict(new_resource)

print("\n" + "=" * 60)
print("PREDICTION RESULT")
print("=" * 60)
print("Predicted Cloud Cost : ₹", round(predicted_cost[0], 2))
print("\nPhase 5 Completed Successfully")