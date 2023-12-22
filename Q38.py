def create_square_list():
    # Use a list comprehension to create a list of squares of numbers from 1 to 30
    square_list = [i**2 for i in range(1, 31)]
    return square_list

# Call the function to create the square list
result_list = create_square_list()

# Print the resulting list
print(result_list)
