
# slip 5: Write a python program to implement Multiple Linear Regression for given dataset.

from pandas.io.formats import style
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression

df=pd.read_csv('cars.csv')

#df.head(5)  # print first 5 data
#print(df)

x=df[['debt','income']]
print(x)
y=df['sales']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
MLR=LinearRegression()

MLR.fit(x_train,y_train)
print("intercept",MLR.intercept_)
print("coefficient",MLR.coef_)

pr=MLR.predict(x_test)
print(pr)