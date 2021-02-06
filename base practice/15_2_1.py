import matplotlib.pyplot as plt
import pandas_datareader.data as web

sk_hynix = web.DataReader("000660.KS", "yahoo")
fig = plt.figure(figsize=(12, 8))

top_axes = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
# 4X4 그리드 안에서 0,0을 기준으로 행방향 3 , 열방향 4
bottom_axes = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)
# 4X4 그리드 안에서 3,0을 기준으로 행방향 1, 열방향 4
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)
#큰값의 거래량이 발생할때 오일러 상수(e)의 지수 형태 표현되지 않게함.
#값이 너무 커지면 범위를 1.000000e+15 이런식으로 바꾸는것이 과학적 표기인데
#직관적으로 볼수있도록 과학적 표기를 해제하는것
top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], label="Adjusted Close")
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'])

plt.tight_layout()
plt.show()