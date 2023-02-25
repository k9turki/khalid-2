import pandas as pd
from sklearn.model_selection import train_test_split

dict= {
    "X" : [i for i in range (-1000,1000 )],
    "Y" : [i for i in range (-1000,1000 )],

}
df= pd.DataFrame(dict)
df["output"]= df["X"]
