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

# --------------------------------------------------
# Clean Fund Master
# --------------------------------------------------

fund = pd.read_csv(
    raw_path / "01_fund_master.csv"
)
print("\nFund Master Shape:")
print(fund.shape)

print("\nFund Master Columns:")
print(fund.columns.tolist())

print("\nMissing Values:")
print(fund.isnull().sum())

print("\nDuplicate Rows:")
print(fund.duplicated().sum())

# Convert launch date to datetime
fund["launch_date"] = pd.to_datetime(
    fund["launch_date"]
)

text_cols = [
    "fund_house",
    "scheme_name",
    "category",
    "sub_category",
    "plan",
    "benchmark",
    "fund_manager",
    "risk_category",
    "sebi_category_code"
]

for col in text_cols:
    fund[col] = fund[col].str.strip()
    
    fund.to_csv(
    processed_path / "01_fund_master_clean.csv",
    index=False
)

print("Fund Master Cleaned")

# --------------------------------------------------
# Clean AUM by Fund House
# --------------------------------------------------

aum = pd.read_csv(
    raw_path / "03_aum_by_fund_house.csv"
)

print("\nAUM Dataset Shape:")
print(aum.shape)

print("\nAUM Dataset Columns:")
print(aum.columns.tolist())

print("\nMissing Values:")
print(aum.isnull().sum())

print("\nDuplicate Rows:")
print(aum.duplicated().sum())

# Convert date column to datetime
aum["date"] = pd.to_datetime(aum["date"])

# Remove leading/trailing spaces
aum["fund_house"] = aum["fund_house"].str.strip()

# Keep only positive AUM values
aum = aum[aum["aum_crore"] > 0]

aum.to_csv(
    processed_path / "03_aum_by_fund_house_clean.csv",
    index=False
)

print("AUM Dataset Cleaned")

# --------------------------------------------------
# Clean Monthly SIP Inflows
# --------------------------------------------------

sip = pd.read_csv(
    raw_path / "04_monthly_sip_inflows.csv"
)

print("\nSIP Dataset Shape:")
print(sip.shape)

print("\nSIP Dataset Columns:")
print(sip.columns.tolist())

print("\nMissing Values:")
print(sip.isnull().sum())

print("\nDuplicate Rows:")
print(sip.duplicated().sum())

# Convert month to datetime
sip["month"] = pd.to_datetime(sip["month"])

sip = sip[
    sip["sip_inflow_crore"] > 0
]

# sip["yoy_growth_pct"].fillna(0)

sip.to_csv(
    processed_path / "04_monthly_sip_inflows_clean.csv",
    index=False
)

print("Monthly SIP Inflows Cleaned")
# fillna(0)

# --------------------------------------------------
# Clean Category Inflows
# --------------------------------------------------

category = pd.read_csv(
    raw_path / "05_category_inflows.csv"
)

print("\nCategory Inflows Shape:")
print(category.shape)

print("\nCategory Inflows Columns:")
print(category.columns.tolist())

print("\nMissing Values:")
print(category.isnull().sum())

print("\nDuplicate Rows:")
print(category.duplicated().sum())

# Convert month column to datetime
category["month"] = pd.to_datetime(category["month"])
# Remove leading/trailing spaces
category["category"] = category["category"].str.strip()

category.to_csv(
    processed_path / "05_category_inflows_clean.csv",
    index=False
)

print("Category Inflows Cleaned")

# --------------------------------------------------
# Clean Industry Folio Count
# --------------------------------------------------

folio = pd.read_csv(
    raw_path / "06_industry_folio_count.csv"
)
print("\nIndustry Folio Shape:")
print(folio.shape)

print("\nIndustry Folio Columns:")
print(folio.columns.tolist())

print("\nMissing Values:")
print(folio.isnull().sum())

print("\nDuplicate Rows:")
print(folio.duplicated().sum())

# Convert month column to datetime
folio["month"] = pd.to_datetime(folio["month"])
# Keep only valid folio counts
folio = folio[
    folio["total_folios_crore"] > 0
]

folio.to_csv(
    processed_path / "06_industry_folio_count_clean.csv",
    index=False
)

print("Industry Folio Count Cleaned")

# --------------------------------------------------
# Clean Portfolio Holdings
# --------------------------------------------------

holdings = pd.read_csv(
    raw_path / "09_portfolio_holdings.csv"
)
print("\nPortfolio Holdings Shape:")
print(holdings.shape)

print("\nPortfolio Holdings Columns:")
print(holdings.columns.tolist())

print("\nMissing Values:")
print(holdings.isnull().sum())

print("\nDuplicate Rows:")
print(holdings.duplicated().sum())

# Convert portfolio date to datetime
holdings["portfolio_date"] = pd.to_datetime(
    holdings["portfolio_date"]
)
text_cols = [
    "stock_symbol",
    "stock_name",
    "sector"
]

for col in text_cols:
    holdings[col] = holdings[col].str.strip()
    holdings = holdings[
    holdings["weight_pct"] >= 0
]
    
holdings.to_csv(
    processed_path / "09_portfolio_holdings_clean.csv",
    index=False
)

print("Portfolio Holdings Cleaned")

# --------------------------------------------------
# Clean Benchmark Indices
# --------------------------------------------------

benchmark = pd.read_csv(
    raw_path / "10_benchmark_indices.csv"
)
print("\nBenchmark Shape:")
print(benchmark.shape)

print("\nBenchmark Columns:")
print(benchmark.columns.tolist())

print("\nMissing Values:")
print(benchmark.isnull().sum())

print("\nDuplicate Rows:")
print(benchmark.duplicated().sum())

# Convert date column to datetime
benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)
# Remove extra spaces
benchmark["index_name"] = (
    benchmark["index_name"]
    .str.strip()
)
benchmark = benchmark[
    benchmark["close_value"] > 0
]

benchmark.to_csv(
    processed_path / "10_benchmark_indices_clean.csv",
    index=False
)

print("Benchmark Indices Cleaned")

print("\n========================================")
print(" All 10 datasets cleaned successfully!")
print(" Clean files saved in: data/processed")
print("========================================")