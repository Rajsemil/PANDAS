import pandas as pd 
sr1 = pd.Series([0,1,2])
print(sr1)
sr2 = pd.Series([3,4,5,6,7])
print(sr2)
pd.concat([sr1, sr2])
df1 = pd.DataFrame({'ID': [1,2,3,4],
                  'Name': ['A', 'B', 'C','D'],
                  'Class': [5,6,7,8]})
print(df1)
df2 = pd.DataFrame({'ID': [5,6,7,8],
                  'Name': ['E', 'F', 'G', 'H'],
                  'Class': [9,10,11,12]})
print(df2)
pd.concat([df2, df1])