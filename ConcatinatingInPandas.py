import pandas as pd

data_1 = {
    'Brand_Name': ['Apple', 'Samsung', 'Nokia', 'Motorola'],
    'Model': ['14 pro', 'S22 Ultra', 'N8', 'Edge 30'],
    'Year': [2022, 2021, 2011, 2022]
}

data_2 = {
    'Brand_Name': ['Nothing', 'OnePlus', 'Oppo'],
    'Model': ['Phone 1', 'OnePlus10', 'Reno 8 Pro'],
    'Year': [2022, 2021, 2021]
}

df1 = pd.DataFrame(data_1)
df2 = pd.DataFrame(data_2, index=[4, 5, 6])

res = pd.concat([df1,df2])
print(res)

# Example 2

'''import pandas as pd

data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1, index=[0, 1, 2, 3])

df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])

con = pd.concat([df, df1])

print(con)
'''



