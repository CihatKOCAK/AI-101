import numpy as np

print("--------- 0-D Arrays-----------")
arr = np.array(42)

print(arr) # 42

print("--------- 1-D Arrays-----------")

arr = np.array([1, 2, 3, 4, 5])

print(arr) # [1 2 3 4 5]

print("--------- 2-D Arrays-----------")


arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr) 
# [[1 2 3] 
# [4 5 6]]

print("--------- 3-D Arrays-----------")


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr) 
# [[1 2 3] 
# [4 5 6]]
# [[1 2 3] 
# [4 5 6]]



# Check Number of Dimensions?
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]]) # 2-D array - square
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # 3-D array - cube

print(a.ndim) # 0
print(b.ndim) # 1
print(c.ndim) # 2
print(d.ndim) # 3