import pandas as pd
import numpy as np
import os
os.chdir(f"D:\Python Practice\FirstProgram")
# l=[1,2,3,4]
# print(pd.DataFrame(l))

dict=pd.DataFrame({"s":pd.Series([1,2,3,4,5]),"a":pd.Series([1,2,3,4,5])})

dict["c"]=dict["a"]+dict["s"]

dict["d"]=dict["a"]>1
# print(dict)

# dict.to_csv("test_file.csv",index=False)
# print(pd.read_csv("test_file.csv",nrows=1))
# print(pd.read_csv("test_file.csv",usecols=[]))
# print(pd.read_csv("test_file.csv",skiprows=[0]))
# print(pd.read_csv("test_file.csv",index_col=1))
# print(pd.read_csv("test_file.csv",header=2))
# print(pd.read_csv("test_file.csv",header=None,names=["a","b","c","d"]))
# print(dict.index)
# print(dict.columns)
# print(dict.head(2))
# print(dict.tail(2))
# print(dict[:5])
# print(np.asarray(dict))
# print(dict.sort_index(axis=0,ascending=False))
# dict.loc[0,'s']=2
# print(dict)
# dict.drop("a",axis=1)
# print(dict)

dict.dropna(axis=0)#row
dict.dropna(axis=1)#column
dict.dropna(how="all")
dict.dropna(subset=["a"])



dict.fillna("a":1,"s":2)
dict.fillna(method="ffill")
dict.fillna(method="bfill")




print(dict)




