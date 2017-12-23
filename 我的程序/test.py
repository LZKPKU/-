#coding:utf-8
import os
import numpy as np
import pandas as pd
from sklearn import ensemble as es
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse_
from sklearn import neural_network as nn
from sklearn.model_selection import GridSearchCV
from sklearn.kernel_ridge import KernelRidge

# Files
name_test="xgb_2"
suffix=".csv"


file_coef="E:\\houseprice\\coef_"+name_test+suffix
file_source="E:\\houseprice\\8_2_All_1.csv"
file_result="E:\\houseprice\\rst_"+name_test+suffix
file_resi="E:\\houseprice\\resi_"+name_test+suffix

# Model
param_grid={
    "n_estimators":[100,200,500,1000,2000,5000],
    "max_samples":[1.0,0.5,0.8],
    "max_features":[1.0,0.5,0.8],
    "warm_start":[True,False],
}
model=GridSearchCV(es.BaggingRegressor(),cv = 5, param_grid = param_grid, scoring='neg_mean_squared_error')
#AdaBoostRegressor(base_estimator=None, learning_rate=1, loss='square',n_estimators=2000, random_state=None)
remove = range(26)

# One-hot Coding
data = pd.read_csv(file_source)

cate_cols=["MSZoning","Street","Alley","LotShape","LandContour","LotConfig","LandSlope","Neighborhood","Condition1","Condition2","BldgType","HouseStyle","RoofStyle","Exterior1st","Exterior2nd","MasVnrType","Foundation","CentralAir","Electrical","SaleType","SaleCondition","PoolQC"]
for i in cate_cols:
    dfi=pd.get_dummies(data[i],prefix=i,drop_first=True)
    data=pd.concat([data,dfi],axis=1)

# Data Splitting
train=data[data['test']==0]
print(train.shape)
test=data[data['test']==1]
print(test.shape)
cols=train.columns.values
colsx=np.delete(cols,remove)

# Fitting models
trainX=train[colsx]
testX=test[colsx]
#trainY=train['LogSalePrice']
trainY = train['SalePrice']
model.fit(trainX, trainY)

# Predicting & Output
print(model.best_estimator_)
rst = pd.DataFrame(model.predict(testX))
#rst['id']=np.array(test['Id'])
rst.to_csv(file_result, sep=',', header=None, index=None)
