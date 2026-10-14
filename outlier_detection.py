"""
VEDA TECHNOLOGY — Level 1, Day 28
Project: Outlier Detection using a Box Plot
Author: AYUSH RAJPUT

Run:
    pip install -r requirements.txt
    python outlier_detection.py
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "employee_salary_dataset.csv"
COLUMN = "Salary_LPA"

def main():
    df = pd.read_csv(DATA_FILE)

    # Calculate outlier limits using the IQR method
    q1 = df[COLUMN].quantile(0.25)
    q3 = df[COLUMN].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = df[(df[COLUMN] < lower_bound) | (df[COLUMN] > upper_bound)]

    print("VEDA TECHNOLOGY — OUTLIER DETECTION")
    print("-" * 42)
    print(f"Dataset rows: {len(df)}")
    print(f"Variable analyzed: {COLUMN}")
    print(f"Q1: {q1:.2f} LPA")
    print(f"Q3: {q3:.2f} LPA")
    print(f"IQR: {iqr:.2f} LPA")
    print(f"Lower bound: {lower_bound:.2f} LPA")
    print(f"Upper bound: {upper_bound:.2f} LPA")

    if outliers.empty:
        print("\\nNo potential outliers were detected.")
    else:
        print("\\nPotential outliers:")
        print(outliers[["Employee_ID", "Department", COLUMN]].to_string(index=False))

    # Save a box plot image
    plt.figure(figsize=(8, 5))
    plt.boxplot(df[COLUMN], vert=True, patch_artist=True)
    plt.title("Employee Salary Box Plot — Outlier Detection")
    plt.ylabel("Salary (LPA)")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("box_plot.png", dpi=160)
    print("\\nBox plot saved as box_plot.png")

    # Save identified outliers for review
    outliers.to_csv("identified_outliers.csv", index=False)
    print("Outlier records saved as identified_outliers.csv")
    print("\\nNote: Do not remove outliers automatically; verify them first.")

if __name__ == "__main__":
    main()
