import pandas as pd
df1 = pd.DataFrame({'A': [1,2,3],
                   'B': [10,20,30]})


df2 = pd.DataFrame({'C': [4,5,6],
                   'D': [40,50,60]})
print(df1)
print(df2)
print(df1, df2)
df1.join(df2)