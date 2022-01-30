import numpy as np
from numpy.random import randn
import pandas as pd


# series

labels = ['a','b','c']
my_data = [1,2,3]
arr = np.array(my_data)
d = {'a':1,'b':2,'c':3}

pd.Series(data = my_data)
# 0    1
# 1    2
# 2    3
# dtype: int64

pd.Series(data=my_data,index=labels) #pd.Series(data,index)
# a    1
# b    2
# c    3
# dtype: int64

pd.Series(my_data,labels)

pd.Series(labels)
# 0    a
# 1    b
# 2    c
# dtype: object

pd.Series(arr)
# 0    1
# 1    2
# 2    3
# dtype: int32

pd.Series(arr,labels) # using arrays
# a    1
# b    2
# c    3
# dtype: int32

pd.Series(d) # using dictionaries
# a    1
# b    2
# c    3
# dtype: int64

pd.Series(data = [print,range,len]) # we can use inbuilt functions and build references to the fucntions
# 0    <built-in function print>
# 1              <class 'range'>
# 2      <built-in function len>
# dtype: object


# indexing

ser1 = pd.Series([1,2,3],['Jaipur','Mumbai','Delhi'])
ser1['Mumbai'] # indexing like dictionary - 2

ser2 = pd.Series([1,2,3],['Jaipur','Mumbai','Banglore'])

ser1 + ser2 # adds the data and puts null value to ones whose index doesn't match
# Banglore    NaN
# Delhi       NaN
# Jaipur      2.0
# Mumbai      4.0
# dtype: float64

