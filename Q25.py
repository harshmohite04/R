def print_alternate_elements(input_list):
    alternate_elements = input_list[::2]
    print("Alternate Elements of the List:")
    for element in alternate_elements:
        print(element)


# Take input from the user for the list
try:
    user_input = input("Enter a list of elements (comma-separated): ")

    # Convert the user input to a list
    user_list = [int(item) if item.isdigit() else item for item in user_input.split(',')]

    # Call the function to print alternate elements
    print_alternate_elements(user_list)

except ValueError:
    print("Invalid input. Please enter a valid list of elements.")
