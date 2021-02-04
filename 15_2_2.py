import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.ticker as ticker

start=datetime.datetime(2016, 3, 1)
end=datetime.datetime(2016, 3, 31)
skhynix = web.DataReader("000660.KS","yahoo", start, end)
skhynix = skhynix[skhynix['Volume']>0]



mc = mpf.make_marketcolors(up='r', down='b')
#상승은 red, 하락 blue
s = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(skhynix, type="", volume=True, style=s)
#mav 이동평균 5일 10일 20일 60일
