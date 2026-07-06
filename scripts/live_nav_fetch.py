import pandas as pd
import requests
from pathlib import Path

scheme_codes = {
    "hdfc_top_100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

output_dir = Path("data/raw")
output_dir.mkdir(exist_ok=True)

for scheme, code in scheme_codes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = output_dir / f"{scheme}_live_nav.csv"
        nav_df.to_csv(file_name, index=False)

        print(f"✓ Saved: {file_name}")

    except Exception as e:
        print(f"✗ Error fetching {scheme}: {e}")