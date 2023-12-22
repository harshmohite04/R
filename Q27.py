import numpy as np

# Given NumPy array
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# Case 1: Sort array by the second row
sorted_array_case1 = sampleArray[:, sampleArray[1, :].argsort()]

# Case 2: Sort the array by the second column
sorted_array_case2 = sampleArray[sampleArray[:, 1].argsort()]

# Display the original and sorted arrays
print("Original Array:")
print(sampleArray)

print("\nSorted Array by the Second Row:")
print(sorted_array_case1)

print("\nSorted Array by the Second Column:")
print(sorted_array_case2)
