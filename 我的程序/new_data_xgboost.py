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
import xgboost as xgb

# Files
name_test="xgb_1"
suffix=".csv"


file_coef="E:\\houseprice\\coef_"+name_test+suffix
file_source="E:\\houseprice\\8_2_All_1.csv"
file_result="E:\\houseprice\\rst_"+name_test+suffix
file_resi="E:\\houseprice\\resi_"+name_test+suffix

# Model
#model = nn.MLPRegressor(hidden_layer_sizes=(100,50,20),activation='logistic')
#model = linear_model.LassoCV(cv = 5)
#model = linear_model.RidgeCV(cv=5)

param_grid={
    "learning_rate":[0.1,0.2,0.05],
    "n_estimators":[1000,2000,5000,500,200,100],
    "silent":[True,False],
    "max_depth":[3,5,7,9],
    "colsample_bytree":[0.5,0.6,0.7,0.8,0.9],
    "objective":["reg:linear"],
    "subsample":[0.5,0.6,0.7,0.8,0.9]
}
model=GridSearchCV(xgb.XGBRegressor(),cv = 5, param_grid = param_grid, scoring='neg_mean_squared_error')
#model = es.GradientBoostingRegressor(loss='ls', learning_rate=0.10, n_estimators=1000, subsample=1.0, criterion='friedman_mse', min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3, min_impurity_split=None, init=None, random_state=None, max_features=None, alpha=0.9, verbose=0, max_leaf_nodes=None, warm_start=False, presort='auto')
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
rst = pd.DataFrame(model.predict(testX))
#rst['id']=np.array(test['Id'])
rst.to_csv(file_result, sep=',', header=None, index=None)
