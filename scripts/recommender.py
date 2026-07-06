'''
import pandas as pd

funds = pd.read_csv("data/processed/07_scheme_performance_clean.csv")


def recommend_funds(risk_level):

    filtered = funds[
        funds["risk_grade"].str.lower() == risk_level.lower()
    ]

    recommendations = (
        filtered.sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return recommendations[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio",
            "return_5yr_pct"
        ]
    ]


risk = input("Enter Risk Appetite (Low / Moderate / High): ")

print(recommend_funds(risk))

'''

import pandas as pd

# Load the cleaned scheme performance dataset
funds = pd.read_csv("data/processed/07_scheme_performance_clean.csv")


def recommend_funds(risk_level):
    """
    Recommend the top 3 mutual funds based on
    risk appetite and highest Sharpe Ratio.
    """

    risk_level = risk_level.strip().lower()

    # Map user input to dataset risk grades
    if risk_level == "low":
        filtered = funds[
            funds["risk_grade"] == "Low"
        ]

    elif risk_level == "moderate":
        filtered = funds[
            funds["risk_grade"].isin(
                ["Moderate", "Moderately High"]
            )
        ]

    elif risk_level == "high":
        filtered = funds[
            funds["risk_grade"].isin(
                ["High", "Very High"]
            )
        ]

    else:
        print("\nInvalid Risk Appetite!")
        print("Please enter one of the following:")
        print("Low")
        print("Moderate")
        print("High")
        return

    recommendations = (
        filtered.sort_values(
            by="sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    print("\nTop 3 Recommended Mutual Funds\n")
    print(
        recommendations[
            [
                "scheme_name",
                "fund_house",
                "category",
                "risk_grade",
                "sharpe_ratio",
                "return_5yr_pct"
            ]
        ].to_string(index=False)
    )


# -----------------------------
# Main Program
# -----------------------------

print("=" * 50)
print("      Bluestock Mutual Fund Recommender")
print("=" * 50)

risk = input("\nEnter Risk Appetite (Low / Moderate / High): ")

recommend_funds(risk)

print("-----------------------------------------------------")
print(funds["risk_grade"].value_counts())