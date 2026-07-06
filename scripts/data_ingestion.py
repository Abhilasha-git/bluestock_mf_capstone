import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
csv_files = sorted(raw_path.glob("*.csv"))

dataframes = {}  # ← MUST add this before the loop

for file in csv_files:
    print("\n" + "=" * 80)
    print(f"FILE: {file.name}")

    try:
        df = pd.read_csv(file)
        dataframes[file.name] = df  # ← store each df as it loads

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")

# ── Task 6: Fund Master Exploration ──────────────────────────────────────────
# ← This entire block was inside except — now correctly outside the loop

print("\n" + "=" * 80)
print("FUND MASTER EXPLORATION")
print("=" * 80)

fund_master = dataframes.get("01_fund_master.csv")  # ← reuse, don't reload

if fund_master is not None:
    print("\nUnique Fund Houses:")
    print(fund_master["fund_house"].unique())

    print("\nUnique Categories:")
    print(fund_master["category"].unique())

    print("\nUnique Sub Categories:")
    print(fund_master["sub_category"].unique())

    print("\nUnique Risk Categories:")
    print(fund_master["risk_category"].unique())
else:
    print("01_fund_master.csv not loaded — check data/raw/")

# ── Task 7: AMFI Code Validation ─────────────────────────────────────────────

print("\n" + "=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

nav_history = dataframes.get("02_nav_history.csv")  # ← now works, dict exists

if fund_master is not None and nav_history is not None:
    fund_codes   = set(fund_master["amfi_code"])
    nav_codes    = set(nav_history["amfi_code"])
    missing_codes = fund_codes - nav_codes

    print(f"\nFund Master codes : {len(fund_codes)}")
    print(f"NAV History codes : {len(nav_codes)}")

    if len(missing_codes) == 0:
        print("\n✓ All AMFI codes in fund_master exist in nav_history")
    else:
        print(f"\n⚠ {len(missing_codes)} codes in fund_master missing from nav_history:")
        print(missing_codes)
else:
    print("Required files not loaded.")