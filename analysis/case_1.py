import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('car data.csv')
df['string']= df['Selling_Price'].astype(str)
df.info()
df.insert(0, 'MAX', df['Selling_Price'] * 2)
print(df.head())
