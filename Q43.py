import numpy as np

# Create two NumPy arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Add the two arrays
result_array = array1 + array2
print("Result Array (After Addition):")
print(result_array)

# Calculate the square of each element in the result array
result_array_squared = np.square(result_array)
print("\nResult Array (After Squaring Each Element):")
print(result_array_squared)

# Generate the transposition of the result array
transposed_array = np.transpose(result_array)
print("\nTransposed Array:")
print(transposed_array)
