import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("diabetes.csv")
df.loc[df['BloodPressure'] == 0, 'BloodPressure'] = 72
train, test = train_test_split(df, test_size=0.2)
train = pd.DataFrame(train)
x_train = train.drop(columns=['Outcome'], axis=1)
y_train = train['Outcome']
train = pd.DataFrame(train)
x_test = test.drop(columns=['Outcome'], axis=1)
y_test = test['Outcome']
model = LogisticRegression(max_iter=10000)
model.fit(x_train, y_train)
predict= model.predict(x_test)

print(predict)
print(y_test)
print(accuracy_score(y_test,predict))

