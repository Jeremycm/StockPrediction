import numpy as np
import pandas as pd
from scipy import stats, integrate
import statistics as st
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
print("start")

data = pd.read_csv('data/EPSGrowth.csv',sep=',',header=None,names=['date','epsg'])
# occurrences = Counter(data['epsg'])
# print(occurrences)
fileter_extreme = list(filter(lambda x: 200 > x > -100, data['epsg']))
# print(fileter_extreme.__len__())
# print(data['epsg'].__len__())
print("mean:" + str(st.mean(fileter_extreme)))
print("median:" + str(st.median(fileter_extreme)))
# print(st.mode(fileter_extreme))
print("percentil: " + str(stats.percentileofscore(fileter_extreme,25.34)))


fileter_extreme = pd.Series(fileter_extreme,name="EPSG'(filter extreme)")
sns.distplot(fileter_extreme)
plt.show()
print("end")
