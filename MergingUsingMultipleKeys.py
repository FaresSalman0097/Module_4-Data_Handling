import pandas as pd

data_1 = {
    'Key1': ['K1', 'K2', 'K3', 'K4'],
    'Key2': ['K5', 'K6', 'K7', 'K8'],
    'TeamAus': ['Smith', 'Finch', 'Johnson', 'Wade'],
    'IplTeam': ['Chennai', 'Bangalore', 'Mumbai', 'Kolkata']
}

data_2 = {
    'Key1': ['K1', 'K2', 'K3', 'K4'],
    'Key2': ['K5', 'K0', 'K7', 'K0'],
    'Age': [32, 35, 40, 37],
    'Rank': [1, 2, 3, 8]
}

df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)

# res = pd.merge(df_1, df_2, on=['Key1', 'Key2'])
# print(res)

# inner - output only matching keys
# res_1 = pd.merge(df_1, df_2, how='inner', on=['Key1', 'Key2'])
# print(res_1)

# outer - output every row in DataFrames with null values which has no matching keys
# res_2 = pd.merge(df_1, df_2, how='outer', on=['Key1', 'Key2'])
# print(res_2)

# left
# res_3 = pd.merge(df_1, df_2, how='left', on=['Key1', 'Key2'])
# print(res_3)

# right
res_4 = pd.merge(df_1, df_2, how='right', on=['Key1', 'Key2'])
print(res_4)