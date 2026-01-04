import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf
 
# Set up Yahoo Finance API
yf.pdr_override()
 
# Import data
def get_data(stocks, start, end):
    stockData = yf.download(stocks, start=start, end=end)['Adj Close']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix
 
stockList = ["NVDA", "AAPL", "NFLX", "META", "MSFT", "TSLA"]
stocks = [stock for stock in stockList]
 
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)
 
meanReturns, covMatrix = get_data(stocks, startDate, endDate)
 
weights = np.random.random(len(meanReturns))
weights /= np.sum(weights)
 
# Monte Carlo method
# Number of simulations
mc_sims = 100
T = 100  # Timeframe in days
 
meanM = np.full(shape=(T, len(weights)), fill_value=meanReturns)
meanM = meanM.T
 
portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0)
 
initialPortfolio = 100000
for m in range(0, mc_sims):
    # MC loops
    Z = np.random.normal(size=(T, len(weights)))
    L = np.linalg.cholesky(covMatrix)
    dailyReturns = meanM + np.inner(L, Z)
    portfolio_sims[:, m] = np.cumprod(np.inner(weights, dailyReturns.T) + 1) * initialPortfolio
 
plt.plot(portfolio_sims)
plt.ylabel("Portfolio Value")
plt.xlabel("Days")
plt.title("MC sim of a stock portfolio")
plt.show()