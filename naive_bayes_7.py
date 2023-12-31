
# slip 7: Write a python program to implement Naive Bayes.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
dataset=pd.read_csv('suv_data.csv')
x=dataset.iloc[:,[2,3]].values
y=dataset.iloc[:,4].values
#print(dataset)
#print(x)
#print(y)

from sklearn.model_selection import train_test_split
#feature scalling
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

#print(x_train)
#print(x_test)

from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(x_train,y_train)
GaussianNB(priors=None,var_smoothing=1e-09)
#predicating the test set results
y_pred=classifier.predict(x_test)
print(y_pred)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)
from sklearn.metrics import accuracy_score
print("Accuracy",accuracy_score(y_test,y_pred))

# 7+3 are incorrct prediction and 65+25 are correct prediction