from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. PROJECT PATHS
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_DIR / "notebooks" / "Online Retail.xlsx"
print("Looking for dataset at:", DATA_PATH)
print("File exists:", DATA_PATH.exists())
REPORTS_DIR = PROJECT_DIR / "reports"
CHARTS_DIR = REPORTS_DIR / "charts"

REPORTS_DIR.mkdir(exist_ok=True)
CHARTS_DIR.mkdir(exist_ok=True)

# ==========================================
# 2. LOAD DATA
# ==========================================

df = pd.read_excel(DATA_PATH)

print("Original dataset:", df.shape)

# ==========================================
# 3. DATA CLEANING
# ==========================================

clean_df = df.copy()

clean_df = clean_df.drop_duplicates()
clean_df = clean_df.dropna(subset=["CustomerID"])

clean_df = clean_df[
    (clean_df["Quantity"] > 0) &
    (clean_df["UnitPrice"] > 0)
].copy()

clean_df["TotalAmount"] = (
    clean_df["Quantity"] * clean_df["UnitPrice"]
)

print("Cleaned dataset:", clean_df.shape)

# ==========================================
# 4. RFM ANALYSIS
# ==========================================

reference_date = (
    clean_df["InvoiceDate"].max() + pd.Timedelta(days=1)
)

rfm = clean_df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (
        reference_date - x.max()
    ).days,
    "InvoiceNo": "nunique",
    "TotalAmount": "sum"
})

rfm.rename(columns={
    "InvoiceDate": "Recency",
    "InvoiceNo": "Frequency",
    "TotalAmount": "Monetary"
}, inplace=True)

rfm = rfm.reset_index()

# ==========================================
# 5. RFM SCORING
# ==========================================

r_rank = rfm["Recency"].rank(pct=True)
f_rank = rfm["Frequency"].rank(pct=True)
m_rank = rfm["Monetary"].rank(pct=True)

bins = [0, 0.2, 0.4, 0.6, 0.8, 1]

rfm["R_Score"] = pd.cut(
    r_rank, bins=bins,
    labels=[5, 4, 3, 2, 1],
    include_lowest=True
).astype(int)

rfm["F_Score"] = pd.cut(
    f_rank, bins=bins,
    labels=[1, 2, 3, 4, 5],
    include_lowest=True
).astype(int)

rfm["M_Score"] = pd.cut(
    m_rank, bins=bins,
    labels=[1, 2, 3, 4, 5],
    include_lowest=True
).astype(int)

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)

# ==========================================
# 6. CUSTOMER SEGMENTATION
# ==========================================

conditions = [
    (rfm["R_Score"] >= 4) &
    (rfm["F_Score"] >= 4) &
    (rfm["M_Score"] >= 4),

    (rfm["R_Score"] >= 3) &
    (rfm["F_Score"] >= 4),

    (rfm["R_Score"] >= 4) &
    (rfm["F_Score"] >= 2),

    (rfm["R_Score"] <= 2) &
    (rfm["F_Score"] >= 3),

    (rfm["R_Score"] <= 2) &
    (rfm["F_Score"] <= 2)
]

labels = [
    "Champions",
    "Loyal Customers",
    "Potential Loyalists",
    "At-Risk Customers",
    "Hibernating Customers"
]

rfm["Segment"] = np.select(
    conditions,
    labels,
    default="Regular Customers"
)

# ==========================================
# 7. SAVE CUSTOMER RFM TABLE
# ==========================================

rfm.to_csv(
    REPORTS_DIR / "customer_rfm.csv",
    index=False
)

# ==========================================
# 8. SEGMENT ANALYSIS
# ==========================================

segment_profile = rfm.groupby("Segment").agg({
    "CustomerID": "count",
    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": "mean"
}).round(2)

segment_distribution = (
    rfm["Segment"].value_counts()
)

segment_revenue = (
    rfm.groupby("Segment")["Monetary"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCUSTOMER SEGMENT PROFILE")
print(segment_profile)

print("\nCUSTOMER DISTRIBUTION")
print(segment_distribution)

print("\nSEGMENT REVENUE")
print(segment_revenue.round(2))

# ==========================================
# 9. CHART 1: CUSTOMER DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

segment_distribution.plot(
    kind="bar",
    title="Customer Distribution by Segment"
)

plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "customer_distribution.png",
    dpi=300
)
plt.close()

# ==========================================
# 10. CHART 2: REVENUE BY SEGMENT
# ==========================================

plt.figure(figsize=(10, 6))

segment_revenue.plot(
    kind="bar",
    title="Revenue Contribution by Customer Segment"
)

plt.xlabel("Customer Segment")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "segment_revenue.png",
    dpi=300
)
plt.close()

# ==========================================
# 11. CHART 3: TOP 10 COUNTRIES
# ==========================================

country_revenue = (
    clean_df.groupby("Country")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

country_revenue.sort_values().plot(
    kind="barh",
    title="Top 10 Countries by Revenue"
)

plt.xlabel("Revenue (£)")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "top_10_countries.png",
    dpi=300
)
plt.close()

# ==========================================
# 12. CHART 4: MONTHLY REVENUE TREND
# ==========================================

monthly_revenue = (
    clean_df.set_index("InvoiceDate")["TotalAmount"]
    .resample("ME")
    .sum()
)

plt.figure(figsize=(12, 6))

monthly_revenue.plot(
    kind="line",
    marker="o",
    title="Monthly Revenue Trend"
)

plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.tight_layout()

plt.savefig(
    CHARTS_DIR / "monthly_revenue_trend.png",
    dpi=300
)
plt.close()

# ==========================================
# 13. FINAL SUMMARY
# ==========================================

print("\nFINAL PROJECT SUMMARY")
print("---------------------")

print("Original records:", len(df))
print("Cleaned records:", len(clean_df))
print("Rows removed:", len(df) - len(clean_df))
print("Unique customers:", rfm["CustomerID"].nunique())

print(
    "Total positive sales: £",
    round(clean_df["TotalAmount"].sum(), 2)
)

print(
    "Highest revenue month:",
    monthly_revenue.idxmax(),
    round(monthly_revenue.max(), 2)
)

print(
    "Lowest revenue month:",
    monthly_revenue.idxmin(),
    round(monthly_revenue.min(), 2)
)

print("\nAnalysis completed successfully!")
print("Results saved in the reports folder.")