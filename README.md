# Quantitative Models in Wharton Investment Competition

## Decription
Mean Variance optimization and Efficient Frontier - The weights of our stock allocations were determined by a Mean-Variance-Optimization (MVO), which we wrote in R. We inputted all our stocks except EDR, (which lacked sufficient historical data) and returned an efficient frontier from which we chose the optimal stock allocation with the minimum risk for a set return. Our 15% low-beta equity is equally composed of indexing ETFs from our five invested sectors, and JEPI, a market-tracking index. Through diversification, would mitigate our risk and capitalize on broader gain in the sector. Finally, the remaining 10% of our allocation went to 10-year treasury bonds due to their record-high rates of 4.9%. Above is our allocation backtested to 2014. We generally outperform the SPDR ETF. 

<img width="805" height="541" alt="image" src="https://github.com/user-attachments/assets/c6b58fc6-ae98-4fca-bfbe-d9f150eb3e7b" />

Discounted Cash Flow Model (DCF) - Our long-term valuation utilized a DCF. DCF relies on the assumption that long-term cash flows are predictable, a condition we satisfy. Using the yahooFinance API, we wrote code in Python to evaluate a company based on the past four years of cash flows. From there, we benchmarked a >15% (Rinehart, 2022) undervaluation as a threshold for purchase.

