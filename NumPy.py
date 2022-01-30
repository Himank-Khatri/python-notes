import numpy as np

# arrays
# vectors - 2d, matrices - 3d

my_list = [1,2,3]
arr = np.array(my_list) #array([1, 2, 3])

my_mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
my_mat #array([[1, 2, 3],
            # [4, 5, 6],
            # [7, 8, 9]])

# functions

np.arange(0,10) # arange is like built-in range
np.arange(0,11,2) # start,stop,step - array([ 0,  2,  4,  6,  8, 10])


np.zeros(5) # create array of zeros by .zeros() - array([0., 0., 0., 0., 0.])
np.zeros((4,4)) # enter dimensions in tuple - array([[0., 0., 0., 0.],
                                                   # [0., 0., 0., 0.],
                                                   # [0., 0., 0., 0.],
                                                   # [0., 0., 0., 0.]])
np.ones(5) # .ones() for 1 - array([1., 1., 1., 1., 1.])


np.linspace(0,5,5) # returns evenly spaced points - (start,stop,points) - 
# array([0.  , 1.25, 2.5 , 3.75, 5.  ])

np.eye(3) # return square matrice with diagonal 1s - array([[1., 0., 0.],
                                                          # [0., 1., 0.],
                                                          # [0., 0., 1.]])


np.random.rand(5) # array([0.33722994, 0.86402938, 0.43961308, 0.45333242, 0.6075314 ])
np.random.rand(3,3) # tuple for matrices -  array([[0.41474924, 0.49340128, 0.32172692],
                                                 # [0.54314968, 0.9354276 , 0.14166485],
                                                 # [0.45337688, 0.45355202, 0.7094356 ]])
np.random.randn(3) # returns random values centered around 0 - array([ 2.03100117,  0.25875203, -1.09863298])

np.random.randint(1,100,5) # random between given values (low,high(excluded),size) 
# - array([25,  4, 84, 60, 62])           
                 

# methods in array

arr = np.arange(25) # makes an array
arr.reshape(5,5) # reshapes vectors to matrices

ranarr = np.random.randint(0,50,10)

arr.max() # returns max value
arr.min() #returns min value
ranarr.max()
ranarr.min()

ranarr.argmax() # returns index position of max value
ranarr.argmin() # returns index position of min value

arr.shape # returns the shape of array - (25,)

arr.dtype # returns data type - dtype('int32')


# 1d indexing 

arr = np.arange(0,11)
arr[:5] # array([0, 1, 2, 3, 4])
arr[:5] = 100 # changes values to given value (broadcasting)
arr # array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])

arr = np.arange(0,11)
slice_of_arr = arr[:5]
slice_of_arr[:] = 99
arr # changes slice values of original array to given value 
# array([99, 99, 99, 99, 99,  5,  6,  7,  8,  9, 10])


# 2d indexing
arr_2d = np.array([[10,15,20],[25,30,35],[40,45,50]])
arr_2d[1][2] # 35
arr_2d[1,2] # 35

arr_2d[:2,:2] # [rows,columns] - array([[10, 15],
                                      # [25, 30]])
arr_2d[2:] # array([[40, 45, 50]])


# conditional selection
arr = np.arange(1,11)
bool_arr = arr>5 
bool_arr # # array([False, False, False, False, False,  True,  True,  True,  True,  True])

arr[bool_arr] # returns only true bools - array([ True,  True,  True,  True,  True])
arr[arr>5] # array([ 6,  7,  8,  9, 10])
arr[arr<4] # array([1, 2, 3])


# operations

arr = np.arange(0,11)
arr + arr # adds corresponding array values - array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20])
arr*arr # multiplies - array([  0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100])
arr + 100 # adds int to all values of array - array([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110])

arr/arr # anything divided by zero gives nan(null) - array([nan,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.])
1/arr # returns inf for 0/1 with warning

np.sqrt(arr) # returns square root
np.sin(arr)
np.log(arr) # returns negetive inf for 0
np.max(arr) # 10
np.min(arr) # 0



























