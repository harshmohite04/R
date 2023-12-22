import numpy as np

def add_matrices(matrix1, matrix2):
    result = np.add(matrix1, matrix2)
    return result

def multiply_matrices(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# Example matrices
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Display the original matrices
print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

# Add matrices
result_addition = add_matrices(matrix_a, matrix_b)
print("\nMatrix Addition:")
print(result_addition)

# Multiply matrices
result_multiplication = multiply_matrices(matrix_a, matrix_b)
print("\nMatrix Multiplication:")
print(result_multiplication)
