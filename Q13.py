import pandas as pd

# Sample Series
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

# Addition
addition_result = series1 + series2

# Subtraction
subtraction_result = series1 - series2

# Multiplication
multiplication_result = series1 * series2

# Division
division_result = series1 / series2

# Display the results
print("Series 1:", series1)
print("Series 2:", series2)
print("\nAddition Result:")
print(addition_result)
print("\nSubtraction Result:")
print(subtraction_result)
print("\nMultiplication Result:")
print(multiplication_result)
print("\nDivision Result:")
print(division_result)
