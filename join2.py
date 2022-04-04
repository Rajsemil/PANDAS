import pandas as pd
df1 = pd.DataFrame({'A': [1,2,3],
                   'B': [10,20,30]},
                   index = ['a','b','c'])
 
df2 = pd.DataFrame({'C': [4,5],
                   'D': [40,50]},
                  index = ['a','b'])
 
print(df1, df2)
df1.join(df2, how = 'right')
df1.join(df2, how = 'inner')

