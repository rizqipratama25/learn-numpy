# make array
import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)
# print(type(arr))

# make tuple
# arr = np.array((1, 2, 3, 4, 5))

# print(arr)

# define the number of dimensions
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("number of dimensions : ", arr.ndim)