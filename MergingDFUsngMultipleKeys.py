import pandas as pd

data_1 = {
    'key1': ['K0', 'K1', 'K2', 'K3'],
    'key2': ['K4', 'K5', 'K6', 'K7'],
    'Players': ['Dhoni', 'Rohit', 'DK', 'Ashwin'],
    'Age': [40, 35, 38, 35]
}

data_2 = {
    'key1': ['K0', 'K1', 'K2', 'K3'],
    'key2': ['K4', 'K5', 'K6', 'K7'],
    'Teams': ["CSK", "MI", "RCB", "DC"]
}
df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)

res = pd.merge(df_1, df_2, on=['key1', 'key2'])
print(res)