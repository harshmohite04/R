import numpy as np

def calculate_statistics(numpy_array):
    # Calculate mean, median, and standard deviation
    mean_value = np.mean(numpy_array)
    median_value = np.median(numpy_array)
    std_deviation = np.std(numpy_array)

    return mean_value, median_value, std_deviation

# Take input from the user for the array elements (comma-separated)
try:
    user_input = input("Enter the array elements (comma-separated): ")

    # Convert the user input to a NumPy array
    numpy_array = np.array([float(item) for item in user_input.split(',')])

    # Call the function to calculate statistics
    mean, median, std_dev = calculate_statistics(numpy_array)

    # Display the results
    print("\nCalculated Statistics:")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")

except ValueError:
    print("Invalid input. Please enter a valid array of numeric elements.")
except Exception as e:
    print(f"An error occurred: {e}")
