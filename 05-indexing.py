import numpy as np

#  we can visualize array 2 dimension as table (column and row)
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print('2nd column 1st row : ', arr[0, 1])

# access 3d array
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])

# negative indexing to access an array from the end
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, -4])