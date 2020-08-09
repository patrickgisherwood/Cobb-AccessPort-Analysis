
import os
import pandas as pd
import numpy as np

directory = r'C:\Users\patri\Documents\AccessPort\DataLogs'
filename = r'datalog1.csv'

path = os.path.join(directory, filename)
df = pd.read_csv (path, engine='python')


paramlist = dict()
paramlist = pd.read_csv('ParameterList.csv', engine='python')

print('\n Printing df:')
print(df)
print('\n Printing paramlist:')
print(paramlist)

data = set()
print(paramlist)
for column in paramlist:
    print(column)
    data.add(paramlist.loc[2,column])


print('\n \n printing data columns: ')

