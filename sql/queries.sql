-- 1. Top 5 Funds by AUM
SELECT fund_house, SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. Average NAV per Fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY avg_nav DESC;

-- 3. SIP Inflow Year-over-Year Growth
SELECT month, yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;

-- 4. Transactions by State
SELECT state,
       COUNT(*) AS transaction_count,
       SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with Expense Ratio Below 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Highest 5-Year Return Funds
SELECT scheme_name, return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 7. Average Investment Amount by Transaction Type
SELECT transaction_type,
       AVG(amount_inr) AS avg_amount
FROM investor_transactions
GROUP BY transaction_type;

-- 8. Fund Count by Risk Category
SELECT risk_category,
       COUNT(*) AS total_funds
FROM fund_master
GROUP BY risk_category
ORDER BY total_funds DESC;

-- 9. Top Sectors by Portfolio Weight
SELECT sector,
       SUM(weight_pct) AS total_weight
FROM portfolio_holdings
GROUP BY sector
ORDER BY total_weight DESC;

-- 10. Benchmark Performance Summary
SELECT index_name,
       MIN(close_value) AS min_value,
       MAX(close_value) AS max_value,
       AVG(close_value) AS avg_value
FROM benchmark_indices
GROUP BY index_name;