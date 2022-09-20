import pandas as pd

data = {
    "Name": ["Salman", "Sameera"],
    "Age": [29, 27]
}
df = pd.DataFrame(data)
# print(df)
# print(df.loc[0])
print(df.loc[1, 1])
# print(df["Name"])



