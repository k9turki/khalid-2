import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('car data.csv')
print(df.loc[30: 35])