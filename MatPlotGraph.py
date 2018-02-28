import matplotlib.pyplot as plt
import pandas as pd
# peg_filtered = pd.read_csv('data/S&P 500 PEG greater than 0 no yr2007-10.csv', sep=',', header=None, names=['date', 'peg>0'])
# # plt.plot(data['pe'])
# # plt.axis(data['date'])
# peg_filtered['date'] = pd.to_datetime(peg_filtered['date'])
# peg_filtered = peg_filtered.set_index('date')
# peg_filtered.plot()
# price = pd.read_csv('data/S&P 500 price.csv', sep=',', header=None, names=['date', 'price'])
# price['date'] = pd.to_datetime(price['date'])
# # price = price.set_index('date')
# price.plot()
# # plt.gcf().autofmt_xdate()
# plt.legend()
def two_scales(ax1, time, data1, data2, c1, c2):
    """

    Parameters
    ----------
    ax : axis
        Axis to put two scales on

    time : array-like
        x-axis values for both datasets

    data1: array-like
        Data for left hand scale

    data2 : array-like
        Data for right hand scale

    c1 : color
        Color for line 1

    c2 : color
        Color for line 2

    Returns
    -------
    ax : axis
        Original axis
    ax2 : axis
        New twin axis
    """
    ax2 = ax1.twinx()

    ax1.plot(time, data1, color=c1,marker='x')
    ax1.set_xlabel('date')
    ax1.set_ylabel('price')

    ax2.plot(time, data2, color=c2,marker='o')
    ax2.set_ylabel('filtered_peg_Yr07Included')
    return ax1, ax2

price_vs_peg = pd.read_csv('data/S&P 500 data - price + PEG filtered.csv', sep=',', header=None, names=['date', 'price','filtered_peg'])
price_vs_peg['date'] = pd.to_datetime(price_vs_peg['date'])
fig, ax = plt.subplots();
ax1, ax2 =two_scales(ax,price_vs_peg['date'],price_vs_peg['price'],price_vs_peg['filtered_peg'],'r','b')

def color_y_axis(ax, color):
    """Color your axes."""
    for t in ax.get_yticklabels():
        t.set_color(color)
    return None
color_y_axis(ax1, 'r')
color_y_axis(ax2, 'b')
plt.show()
