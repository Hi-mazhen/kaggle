# import matplotlib.pyplot as plt 
# plt.plot([1,2,3]) 
# plt.ylabel('some numbers') 
# plt.show()

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data_train = pd.read_csv("train.csv")
data_train
data_train.info()
data_train.describe()

# 接下来继续分析数据特征
#    