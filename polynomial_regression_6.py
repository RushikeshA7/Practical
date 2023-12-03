
# slip 6: Write a python program to implement Polynomial Linear Regression for given dataset.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics
dataset=pd.read_csv('position.csv')
dataset

x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values
# print(x)
#print(y)

#Fitting linear regression to the dataset
from sklearn.linear_model import LinearRegression
lin = LinearRegression()
lin.fit(x,y)

#LinearRegression(copy_X=True,fit_intercept=True,n_jobs=None,normalize=False)

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=4)
x_poly =poly.fit_transform(x)
poly.fit(x_poly,y)
lin2=LinearRegression()
lin2.fit(x_poly,y)

#LinearRegression(copy_x=True,fit_intercept=True,n_jobs=None,normalize=False)

plt.scatter(x,y,color ='blue')
plt.plot(x,lin2.predict(poly.fit_transform(x)),color='red')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()