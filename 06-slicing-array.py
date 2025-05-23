import numpy as np

# we pass slice instead of index like this : [start:end]
# we can also define step, like this : [start:end:step]
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:]) # from index 4 to end
print(arr[:4]) # slice elements from the beginning to index 4 (not included)

# step
print(arr[1:5:2])
print(arr[::2])

# slicing 2d array
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2[1, 1:4]) # from the second element, slice element from index 1 to index 4 (not included)

