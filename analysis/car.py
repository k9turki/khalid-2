import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('car data.csv')
'''print(df.head())
print(df['Car_Name'].head())
print(df.tail())
print(df.loc[0])
dic = {
    "column1": [10, 20, 300],
    "column2": [30, 10, 100]

}
df2= pd.DataFrame(dic)
print(df2.head(5))
print(df.shape)'''

'''df.info()
print(df.describe())'''

#df['Selling_Price'].plot()
df["Year"].hist()
df.plot.scatter(x="Year", y="Selling_Price")
plt.show()