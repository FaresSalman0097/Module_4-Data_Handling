import pandas as pd
from datetime import datetime

df = pd.DataFrame({'date': ['3/10/2000', '3/11/2000', '3/12/2000'], 'value': [2, 3, 4]})

# df['date'] = pd.to_datetime(df['date'])   #convert strings to datetime objects

# df['date'] = pd.to_datetime(df['date'],dayfirst=False)

df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y")

print(df)
