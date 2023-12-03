
#Decision Tree
# slip 8: Write a python program to implement Decision Tree whether or not to play Tennis.

import pandas as pd
import numpy as np
PT=pd.read_csv("playtennis.csv")
print(PT)
#From Converting data into 0 1 fromat
from sklearn.preprocessing import LabelEncoder
Le=LabelEncoder()

PT['outlook']=Le.fit_transform(PT['outlook'])
PT['temp']=Le.fit_transform(PT['temp'])
PT['humidity']=Le.fit_transform(PT['humidity'])
PT['windy']=Le.fit_transform(PT['windy'])
PT['play']=Le.fit_transform(PT['play'])

print(PT)

y= PT['play']
x=PT.drop(['play'],axis=1)#for drop the play colume

#making Decision Tree
from sklearn import tree
clf=tree.DecisionTreeClassifier(criterion ='entropy')
clf=clf.fit(x,y)

tree.plot_tree(clf)

#graphical Represention

import graphviz
dot_data =tree.export_graphviz(clf,out_file=None)
graph= graphviz.Source(dot_data)
graph

import pandas as pd
data= pd.DataFrame({"A":[12,4,5,3,1],
                   "B":[5,2,54,3,16],
                   "C":[20,16,7,3,8],
                   "D":[14,3,None,None,6]})

df = pd.DataFrame(data)
print(df)
df.dropna(subset=['D'],inplace=True)
print("This is Ans :")
print(df)

#catagerical into numerical
import numpy as np
import pandas as pd
Playtennis = pd.read_csv("playtennis.csv")

Playtennis

from sklearn.preprocessing import LabelEncoder
Le = LabelEncoder()

Playtennis['outlook']=Le.fit_transform(Playtennis['outlook'])
Playtennis['temp']=Le.fit_transform(Playtennis['temp'])
Playtennis['humidity']=Le.fit_transform(Playtennis['humidity'])
Playtennis['windy']=Le.fit_transform(Playtennis['windy'])
Playtennis['play']=Le.fit_transform(Playtennis['play'])