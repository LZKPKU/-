#coding:utf-8
import numpy as np
import os
import pandas as pd
from sklearn.metrics import mean_squared_error as mse_

#path source
file1 = "E:\\houseprice\\33803.csv"
file2 = "E:\\houseprice\\19502.csv"
save = "E:\\houseprice\\result.csv"

#read data
data1 = pd.read_csv(file1,header = None)
data2 = pd.read_csv(file2,header = None)

#distance
dist1 = 33803
dist2 = 19501
dist = np.sqrt(mse_(data1,data2))

#余弦定理
cos1 = (dist1*dist1 + dist * dist - dist2*dist2)/(2*dist1*dist)
cos2 = (dist2*dist2 + dist * dist - dist1*dist1)/(2*dist2*dist)
w1 = dist1*cos1/dist
w2 = dist2*cos2/dist
result = np.array(data1)*w2+np.array(data2)*w1
result = pd.DataFrame(result)
result.to_csv(save,index = None,header = None)

