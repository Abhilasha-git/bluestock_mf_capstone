"""
ETL Pipeline Runner
Runs all ETL scripts sequentially without modifying them.
"""

import subprocess
import sys
from pathlib import Path

# Project root (one level above the scripts folder)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Scripts to execute in order
SCRIPTS = [
    "scripts/data_ingestion.py",
    "scripts/data_cleaning.py",
    "scripts/sqlite_loader.py"
]


def run_script(script_path):
    script = PROJECT_ROOT / script_path

    print("\n" + "=" * 80)
    print(f"Running: {script.name}")
    print("=" * 80)

    try:
        subprocess.run(
            [sys.executable, str(script)],
            cwd=PROJECT_ROOT,   # Ensures relative paths like data/raw work
            check=True
        )
        print(f"✓ {script.name} completed successfully.")

    except subprocess.CalledProcessError:
        print(f"✗ Error while running {script.name}")
        sys.exit(1)


def main():
    print("\nStarting Bluestock Mutual Fund ETL Pipeline...")

    for script in SCRIPTS:
        run_script(script)

    print("\n" + "=" * 80)
    print("ETL Pipeline completed successfully.")
    print("=" * 80)


if __name__ == "__main__":
    main()