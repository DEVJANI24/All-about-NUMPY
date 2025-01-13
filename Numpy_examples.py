#Array
# 1D Array
arr = np.array([5, 10, 15])
print(arr)

# 2D Array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)


#2. Array Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
print(a + b)

# Broadcasting example
print(a * 2)


#3. Array Indexing and Slicing
arr = np.array([10, 20, 30, 40, 50])

# Indexing
print(arr[2])  # Output: 30

# Slicing
print(arr[1:4])  # Output: [20, 30, 40]
