import pandas as pd
list=['s','m','i','l','e']
ser=pd.Series(list)
print(ser)
print(ser[2])

# Indexing

list1=[1,2,'Three',4,'Five',6]
ser1=pd.Series(list1,index=["First","Second",103,"Fourth",105,"Last"])
print(ser1)
print(ser1['Second'])
print(ser1[105])