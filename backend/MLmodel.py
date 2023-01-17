# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 17:18:13 2023

@author: hp
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
import pickle
scale = StandardScaler()
df = pd.read_csv('gpu_train.csv')
X = df[['price', 'rating']]
Y = df['reviews']
X[['price', 'rating']] = scale.fit_transform(X[['price','rating']].values)
X = sm.add_constant(X)
est = sm.OLS(Y, X).fit()
orgdata = pd.read_csv('data.csv')
x = []
y = []
for i in range(len(orgdata)):
    scaled = scale.transform([[orgdata['price'][i], orgdata['ratings'][i]]])
    scaled = np.insert(scaled[0], 0, 1)
    predicted = est.predict(scaled)
    if orgdata['ratings'][i] != 0:
        a = ["gpu" + str(i+1),  orgdata['price'][i],  abs(orgdata['reviews'][i] - predicted[0])]
        x.append(a)
    else:
       a = ["gpu" + str(i+1),  orgdata['price'][i],  abs(orgdata['reviews'][i] - predicted[0])]
       y.append(a)
   
arr1 = sorted(x, key= lambda x:x[2], reverse = True)
arr2 = sorted(y, key= lambda y:y[2], reverse = True)
for row in arr2:
    arr1.append(row)

result = []
for row in arr1:
    a = [row[0], row[1]]
    result.append(a)
print(result)
pickle.dump(result,open("model.pkl","wb"))
result.to_pickle("model.pkl")

    




