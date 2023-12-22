import pandas as pd

# Original Data Series
data_series = pd.Series([100, 200, 'python', 300.12, 400])

# Sort the Series
sorted_series = data_series.sort_values()

# Display the original and sorted Series
print("Original Data Series:")
print(data_series)
print("\nSorted Data Series:")
print(sorted_series)
