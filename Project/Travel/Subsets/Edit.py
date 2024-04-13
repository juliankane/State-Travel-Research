import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

poverty = pd.read_csv('poverty.csv')
#print(poverty.index)
print(poverty)
poverty.index=poverty['State']
poverty.drop(columns='State', inplace=True)
poverty.to_csv('poverty2.csv')
