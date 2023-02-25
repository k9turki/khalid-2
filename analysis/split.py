import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


data1=pd.read_csv('diabetes.csv')


X=data1.drop('status',axis=1)
Y=data1['status']
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3)



mod=KNeighborsClassifier()
mod.fit(x_train,y_train)
y_pred=mod.predict(x_test)
print(classification_report(y_test,y_pred))

mod=SVC()
mod.fit(x_train,y_train)
y_pred=mod.predict(x_test)
print(classification_report(y_test,y_pred))

mod=LogisticRegression()
mod.fit(x_train,y_train)
y_pred=mod.predict(x_test)
print(classification_report(y_test,y_pred))

mod=RandomForestClassifier()
mod.fit(x_train,y_train)
y_pred=mod.predict(x_test)
print(classification_report(y_test,y_pred))

mod=DecisionTreeClassifier()
mod.fit(x_train,y_train)
y_pred=mod.predict(x_test)
print(classification_report(y_test,y_pred))

