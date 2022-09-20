import pandas as pd

data_1 = {
    'Key': ['K0', 'K1', 'K2', 'K3'],
    'Name': ['ManiRatnam', 'Vikram', 'Ravi', 'Karthi'],
    'Age': [60, 58, 45, 38]
}
data_2 = {
    'Key': ['K0', 'K1', 'K2', 'K3'],
    'Movies': ['Nayakan', 'Ravanan', 'Thani Oruvan', 'kaithi'],
    'Actress': ['SriDevi', 'Aishwarya Rai', 'Nayanthara', 'Tamannah']
}
df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)

res = pd.merge(df_1, df_2, on='Key')

print(res)
