import pandas as pd
list=['s','m','i','l','e']
ser=pd.Series(list)
print(ser)
# Labels
print(ser[2])

# Indexing

list1=[1,2,'Three',4,'Five',6]
ser1=pd.Series(list1,index=["First","Second",103,"Fourth",105,"Last"])
print(ser1)
print(ser1['Second'])
print(ser1[105])

# Key/value as series

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar1 = pd.Series(calories)
print(myvar1)

# indexing key/value pair
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar2 = pd.Series(calories, index = ["day1", "day2"])
print(myvar2)