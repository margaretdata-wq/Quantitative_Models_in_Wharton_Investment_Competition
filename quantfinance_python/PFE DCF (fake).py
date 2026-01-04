### PFE DCF
# Read stocks
import yfinance as yf

#apple intrinsic value calculations 

#pfe = yf.Ticker("PFE")
outstandingshares = 5646000000 #pfe.info["sharesOutstanding"]

#assumptions
required_rate = 0.07
perpetual_rate = 0.02
cashflowgrowthrate = 0.1311

years = [1,2,3,4]

freecashflow = [9994000, 11612000, 29869000, 26031000] #last 4 years in 1000s

futurefreecashflow = []
discountfactor = []
discountedfuturefreecashflow = []
terminalvalue = freecashflow[-1] * (1+perpetual_rate)/(required_rate-perpetual_rate)

for year in years:
    cashflow = freecashflow[-1] * (1+cashflowgrowthrate)**year
    futurefreecashflow.append(cashflow)
    discountfactor.append((1+required_rate)**year)

#print(discountfactor)
#print(futurefreecashflow)

for i in range(0, len(years)):
    discountedfuturefreecashflow.append(futurefreecashflow[i]/discountfactor[i])

#print(discountedfuturefreecashflow)

discountedterminalvalue = terminalvalue/(1+required_rate)**4 #4 is the number of years 
discountedfuturefreecashflow.append(discountedterminalvalue)

todaysvalue = sum(discountedfuturefreecashflow)

fairvalue = todaysvalue*1000/outstandingshares

print("the fair value is ${}".format(round(fairvalue,2)))


