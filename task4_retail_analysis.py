"""
Task 4 - Real-world Data Project
Retail Sales Analysis

Install:
    pip install pandas numpy matplotlib

Run:
    python task4_retail_analysis.py
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path("retail_sales_dataset.csv")

if not DATA_FILE.exists():
    raise FileNotFoundError("retail_sales_dataset.csv was not found.")

df = pd.read_csv(DATA_FILE)
print("Original dataset shape:", df.shape)
print("\nMissing values:")
print(df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Data cleaning
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])
df["Discount"] = df["Discount"].fillna(df["Discount"].median())
df["Sales"] = df["Sales"].fillna(df["Sales"].median())
df = df.drop_duplicates().copy()

df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
df["Profit_Margin"] = np.where(df["Sales"] > 0, df["Profit"] / df["Sales"] * 100, 0)

# Statistical summary
numeric = ["Units_Sold","Unit_Price","Discount","Sales","Cost","Profit","Profit_Margin"]
df[numeric].describe().T.round(2).to_csv("01_statistical_summary.csv")

# Regional analysis
region = df.groupby("Region").agg(
    Orders=("Region","size"),
    Units=("Units_Sold","sum"),
    Sales=("Sales","sum"),
    Profit=("Profit","sum"),
    Avg_Order_Value=("Sales","mean")
).sort_values("Sales", ascending=False).round(2)
region.to_csv("02_region_analysis.csv")

# Category analysis
category = df.groupby("Category").agg(
    Orders=("Category","size"),
    Units=("Units_Sold","sum"),
    Sales=("Sales","sum"),
    Profit=("Profit","sum")
).sort_values("Sales", ascending=False).round(2)
category.to_csv("03_category_analysis.csv")

# Channel analysis
channel = df.groupby("Channel").agg(
    Orders=("Channel","size"),
    Units=("Units_Sold","sum"),
    Sales=("Sales","sum"),
    Profit=("Profit","sum")
).sort_values("Sales", ascending=False).round(2)
channel.to_csv("04_channel_analysis.csv")

# Monthly trend
monthly = df.groupby("Month").agg(Sales=("Sales","sum"), Profit=("Profit","sum")).reset_index()
monthly.to_csv("05_monthly_trend.csv", index=False)

# Correlation analysis
corr = df[numeric].corr().round(3)
corr.to_csv("06_correlation_matrix.csv")

# Visualizations
monthly.plot(x="Month", y="Sales", legend=False, figsize=(9,5))
plt.title("Monthly Sales Trend")
plt.xlabel("Month"); plt.ylabel("Sales"); plt.xticks(rotation=45)
plt.tight_layout(); plt.savefig("01_monthly_sales_trend.png", dpi=180); plt.close()

category["Sales"].sort_values().plot(kind="barh", figsize=(8,5))
plt.title("Sales by Product Category")
plt.xlabel("Sales"); plt.tight_layout()
plt.savefig("02_sales_by_category.png", dpi=180); plt.close()

region["Profit"].sort_values().plot(kind="bar", figsize=(8,5))
plt.title("Profit by Region")
plt.xlabel("Region"); plt.ylabel("Profit")
plt.tight_layout(); plt.savefig("03_profit_by_region.png", dpi=180); plt.close()

channel["Sales"].plot(kind="bar", figsize=(8,5))
plt.title("Sales by Sales Channel")
plt.xlabel("Channel"); plt.ylabel("Sales"); plt.xticks(rotation=0)
plt.tight_layout(); plt.savefig("04_sales_by_channel.png", dpi=180); plt.close()

plt.figure(figsize=(8,5))
plt.scatter(df["Discount"], df["Profit"], alpha=0.5)
plt.title("Discount vs Profit")
plt.xlabel("Discount"); plt.ylabel("Profit")
plt.tight_layout(); plt.savefig("05_discount_vs_profit.png", dpi=180); plt.close()

plt.figure(figsize=(8,7))
plt.imshow(corr, aspect="auto")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
plt.yticks(range(len(corr.index)), corr.index)
plt.title("Correlation Matrix")
for i in range(len(corr.index)):
    for j in range(len(corr.columns)):
        plt.text(j, i, f"{corr.iloc[i,j]:.2f}", ha="center", va="center", fontsize=7)
plt.colorbar(label="Correlation")
plt.tight_layout(); plt.savefig("06_correlation_matrix.png", dpi=180); plt.close()

print("\nAnalysis completed.")
print("Top category by sales:", category.index[0])
print("Top region by sales:", region.index[0])
print("Top channel by sales:", channel.index[0])
