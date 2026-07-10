# 📊 Bluestock Mutual Fund Analytics & Performance Evaluation

## Overview

The **Bluestock Mutual Fund Analytics & Performance Evaluation** project is an end-to-end data analytics solution developed during my internship at **Bluestock Fintech**. The project focuses on transforming raw mutual fund datasets into meaningful business insights through data engineering, financial analytics, advanced risk analysis, and interactive business intelligence dashboards.

The solution automates the complete analytics pipeline—from data ingestion and cleaning to performance evaluation and dashboard visualization—enabling data-driven investment decision-making.

---

# Project Objectives

- Build an automated ETL pipeline for mutual fund datasets.
- Clean, validate, and standardize raw financial data.
- Design and implement a relational SQLite database.
- Perform Exploratory Data Analysis (EDA).
- Calculate key mutual fund performance metrics.
- Conduct advanced financial and investor analytics.
- Develop an interactive Power BI dashboard.
- Implement a mutual fund recommendation system based on investor risk appetite.

---

# Project Architecture

```
Raw CSV Files
        │
        ▼
 Data Ingestion (Python)
        │
        ▼
 Data Cleaning & Validation
        │
        ▼
 Processed Datasets
        │
        ▼
 SQLite Database
        │
        ▼
 Financial Analytics
        │
        ▼
 Advanced Analytics
        │
        ▼
 Power BI Dashboard
        │
        ▼
 Business Insights
```

---

# Technology Stack

| Category | Tools |
|----------|------|
| Programming | Python |
| Libraries | Pandas, NumPy, Matplotlib, Seaborn |
| Database | SQLite |
| Query Language | SQL |
| Dashboard | Microsoft Power BI |
| Development Environment | Jupyter Notebook, VS Code |
| Version Control | Git & GitHub |

---

# Project Structure

```
mutual-fund-analysis/

├── dashboard/
│   └── Power BI dashboard files
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── docs/
│
├── notebooks/
│   ├── Data Engineering
│   ├── EDA
│   ├── Performance Analytics
│   └── Advanced Analytics
│
├── reports/
│   ├── EDA/
│   ├── performance_metrics/
│   └── advanced_analytics/
│
├── scripts/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── recommender.py
│   └── sqlite_loader.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── Project_Report.pdf
├── Presentation.pptx
├── requirements.txt
└── README.md
```

---

# Data Sources

The project utilizes:

- Mutual Fund Master Dataset
- Historical NAV Dataset
- AUM Dataset
- SIP Inflow Dataset
- Category Inflow Dataset
- Industry Folio Dataset
- Portfolio Holdings Dataset
- Benchmark Dataset
- Investor Transactions Dataset
- Live NAV Data

---

# Features

## Data Engineering

- Automated ETL pipeline
- Data cleaning
- Missing value treatment
- Data validation
- SQLite database implementation

---

## Exploratory Data Analysis

- Investor Demographics
- SIP Trend Analysis
- Category Inflow Analysis
- Sector Allocation
- Industry Trends

---

## Performance Analytics

- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha & Beta
- Maximum Drawdown
- Tracking Error

---

## Advanced Analytics

- Historical VaR & CVaR
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Sector HHI Concentration Analysis
- Fund Recommendation System

---

## Interactive Dashboard

The Power BI dashboard provides:

- Industry Overview
- Fund Performance Analysis
- Investor Analytics
- SIP & Market Trends
- Fund NAV Drill-through Analysis

---

# Key Business Insights

- Equity-oriented mutual funds attracted the highest investor participation.
- SIP investments demonstrated consistent long-term growth.
- Risk-adjusted returns varied significantly across schemes.
- Portfolio diversification reduced sector concentration risk.
- Investor cohort analysis revealed long-term investment behavior.
- The recommendation engine successfully matched mutual funds with investor risk profiles.

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd mutual-fund-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the ETL pipeline:

```bash
python scripts/etl_pipeline.py
```

Execute analytics notebooks from the `notebooks` directory.

Open the Power BI dashboard:

```
dashboard/Mutual_Fund_Analytics.pbix
```

---

# Deliverables

- Automated ETL Pipeline
- SQLite Database
- Exploratory Data Analysis
- Performance Analytics
- Advanced Risk Analytics
- Power BI Dashboard
- Mutual Fund Recommendation System
- Final Project Report
- Presentation

---

# Future Enhancements

- Live data integration through APIs
- Scheduled ETL automation
- Streamlit web application
- Portfolio optimization using Modern Portfolio Theory
- Machine Learning-based fund recommendation
- Automated reporting

---

# Author

**Abhilasha Kumari**

Internship Project

Bluestock Fintech

---

# Acknowledgement

This project was developed as part of the internship program at **Bluestock Fintech**. I sincerely thank the organization and my mentors for their guidance, support, and valuable learning opportunities throughout the project.