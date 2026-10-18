import io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Dataset Load (Local File > Self-Generated Sample Data Fallback)
try:
    df = pd.read_csv("Unemployment_in_India.csv")
    print("SUCCESS: Dataset loaded successfully from local file!")
except FileNotFoundError:
    print("WARNING: Local file not found. Generating sample dataset...")

    # Fixed Equal Length Data (14 rows)
    dates = pd.date_range(start="2019-05-31", periods=14, freq="ME")
    data = {
        "Date": dates,
        "Area": [
            "Rural",
            "Rural",
            "Rural",
            "Rural",
            "Rural",
            "Rural",
            "Rural",
            "Urban",
            "Urban",
            "Urban",
            "Urban",
            "Urban",
            "Urban",
            "Urban",
        ],
        "Estimated Unemployment Rate (%)": [
            3.65,
            3.05,
            3.75,
            3.32,
            5.17,
            3.52,
            4.12,
            16.29,
            15.72,
            12.85,
            10.35,
            8.90,
            9.12,
            7.55,
        ],
    }
    df = pd.DataFrame(data)

# 2. Data Preprocessing
df.columns = df.columns.str.strip()
df = df.dropna()

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])

# 3. Plotting Unemployment Trend
plt.figure(figsize=(12, 6))

hue_col = (
    "Area"
    if "Area" in df.columns
    else ("Region" if "Region" in df.columns else None)
)

sns.lineplot(
    data=df,
    x="Date",
    y="Estimated Unemployment Rate (%)",
    hue=hue_col,
    marker="o",
    linewidth=2.5,
)

plt.title(
    "Unemployment Rate Analysis in India (Including Covid-19 Impact)",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Unemployment Rate (%)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# Save & Show
plt.savefig("unemployment_trend.png", dpi=300)
plt.show()

print("SUCCESS: Unemployment trend plot created and saved successfully!")