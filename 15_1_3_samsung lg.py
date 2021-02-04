import pandas_datareader.data as web
import matplotlib.pyplot as plt

lg = web.DataReader("066570.KS", "yahoo")
samsung = web.DataReader("005930.KS","yahoo")
hyundai = web.DataReader("005380.Ks", "yahoo")

plt.plot(lg.index, lg['Adj Close'], label='LG Electronics')
plt.plot(samsung.index, samsung['Adj Close'], label="Samsung Electronics")
plt.plot(hyundai.index, hyundai['Adj Close'], label="Hyundai Motor Company")

plt.legend(loc="upper left")

plt.show()

