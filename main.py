# ==========================================
# SMART CLOUD COST OPTIMIZER
# Complete Main Program
# ==========================================

print("=" * 60)
print("        SMART CLOUD COST OPTIMIZER")
print("=" * 60)

print("\nLoading Dataset...")
import phase1_dataset
print("\nPhase 1 Completed Successfully")

print("\nRunning Cloud Cost Analysis...")
import phase2_analysis
print("\nPhase 2 Completed Successfully")

print("\nRunning Data Cleaning...")
import phase3_cleaning
print("\nPhase 3 Completed Successfully")

print("\nGenerating Visualizations...")
import phase4_visualization
print("\nPhase 4 Completed Successfully")

print("\nRunning Machine Learning Cost Prediction...")
import phase5_machine_learning
print("\nPhase 5 Completed Successfully")

print("\nGenerating AI Recommendations...")
import phase6_ai_recommendation
print("\nPhase 6 Completed Successfully")

print("\nGenerating Final FinOps Report...")
import phase7_finops_report
print("\nPhase 7 Completed Successfully")

print("\n" + "=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nProject Features:")
print("✔ Dataset Analysis")
print("✔ Data Cleaning")
print("✔ Cost Visualizations")
print("✔ ML Cost Prediction")
print("✔ AI Optimization Recommendations")
print("✔ FinOps Report Export")