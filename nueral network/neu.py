import pandas as pd
from keras import Sequential
from keras.layers import InputLayer, Dense
from sklearn.model_selection import train_test_split
import tensorflow
df = pd.read_csv('diabetes.csv')
train_df, test_df = train_test_split(df, test_size=.3)
train_df = pd.DataFrame(train_df)
train_x = train_df.drop(columns=['Outcome'], axis=1)
train_y = train_df['Outcome']
# model Building
model = Sequential()
model.add(InputLayer(input_shape=train_x.shape[1]))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile
model.compile(optimizer='adam', loss='binary_cross entropy', metrics=['accuracy0'])
model.fit(train_x, train_y, epochs=11)
