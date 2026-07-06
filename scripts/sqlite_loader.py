import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

print("Creating SQLite Database...")

# Database
engine = create_engine("sqlite:///bluestock_mf.db")

# Paths
raw_path = Path("data/raw")
processed_path = Path("data/processed")

# Load datasets
fund_master = pd.read_csv(raw_path / "01_fund_master.csv")
nav_history = pd.read_csv(processed_path / "02_nav_history_clean.csv")
aum = pd.read_csv(raw_path / "03_aum_by_fund_house.csv")
sip = pd.read_csv(raw_path / "04_monthly_sip_inflows.csv")
category = pd.read_csv(raw_path / "05_category_inflows.csv")
folio = pd.read_csv(raw_path / "06_industry_folio_count.csv")
performance = pd.read_csv(processed_path / "07_scheme_performance_clean.csv")
transactions = pd.read_csv(processed_path / "08_investor_transactions_clean.csv")
holdings = pd.read_csv(raw_path / "09_portfolio_holdings.csv")
benchmark = pd.read_csv(raw_path / "10_benchmark_indices.csv")

# Load into SQLite
fund_master.to_sql("fund_master", engine, if_exists="replace", index=False)
nav_history.to_sql("nav_history", engine, if_exists="replace", index=False)
aum.to_sql("aum_by_fund_house", engine, if_exists="replace", index=False)
sip.to_sql("monthly_sip_inflows", engine, if_exists="replace", index=False)
category.to_sql("category_inflows", engine, if_exists="replace", index=False)
folio.to_sql("industry_folio_count", engine, if_exists="replace", index=False)
performance.to_sql("scheme_performance", engine, if_exists="replace", index=False)
transactions.to_sql("investor_transactions", engine, if_exists="replace", index=False)
holdings.to_sql("portfolio_holdings", engine, if_exists="replace", index=False)
benchmark.to_sql("benchmark_indices", engine, if_exists="replace", index=False)

print("Database Loaded Successfully!")

# Verification
print("\nRow Count Verification")

tables = {
    "fund_master": fund_master,
    "nav_history": nav_history,
    "aum_by_fund_house": aum,
    "monthly_sip_inflows": sip,
    "category_inflows": category,
    "industry_folio_count": folio,
    "scheme_performance": performance,
    "investor_transactions": transactions,
    "portfolio_holdings": holdings,
    "benchmark_indices": benchmark
}

for table_name, df in tables.items():
    print(f"{table_name:<25} {len(df):>8} rows")

print("\nbluestock_mf.db created successfully")