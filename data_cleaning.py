import pandas as pd
from pathlib import Path

# Folder paths
raw_path = Path("data/raw")
processed_path = Path("data/processed")

# Create processed folder if it doesn't exist
processed_path.mkdir(parents=True, exist_ok=True)

print("Data Cleaning Started...")

# ==========================
# NAV HISTORY CLEANING
# ==========================

nav = pd.read_csv(raw_path / "02_nav_history.csv")

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sort by AMFI code and date
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicate rows
nav = nav.drop_duplicates()

# Forward-fill missing NAV values within each fund
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Keep only positive NAV values
nav = nav[nav["nav"] > 0]

# Save cleaned file
nav.to_csv(
    processed_path / "02_nav_history_clean.csv",
    index=False
)

print("NAV History Cleaned")

# --------------------------------------------------
# Clean Investor Transactions
# --------------------------------------------------

transactions = pd.read_csv(
    raw_path / "08_investor_transactions.csv"
)

# Fix date format
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Standardize transaction types
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only positive amounts
transactions = transactions[
    transactions["amount_inr"] > 0
]

# Validate KYC values
valid_kyc = ["Verified", "Pending"]

invalid_kyc = transactions[
    ~transactions["kyc_status"].isin(valid_kyc)
]

print("\nInvalid KYC Records:", len(invalid_kyc))

# Save cleaned file
transactions.to_csv(
    processed_path / "08_investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions Cleaned")


# --------------------------------------------------
# Clean Scheme Performance
# --------------------------------------------------

performance = pd.read_csv(
    raw_path / "07_scheme_performance.csv"
)

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_cols:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

# Check for invalid expense ratios
invalid_expense = performance[
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Records:",
      len(invalid_expense))

# Save cleaned file
performance.to_csv(
    processed_path / "07_scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance Cleaned")