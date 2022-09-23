import pandas as pd

data = {
    "Name": ["Salman", "Sameera"],
    "Age": [29, 27]
}
df = pd.DataFrame(data)
#print(df)
# print(df.loc[0])
#print(df.loc[[1, 1]])
#print(df["Name"])

# named indexes
data1 = {
    "Name": ["Vijay", "Vikram"],
    "Age": [48, 54]
}
df1 = pd.DataFrame(data1, index=["Varisu","Cobra"])
print(df1)




