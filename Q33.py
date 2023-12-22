def swap_elements(input_list, index1, index2):
    # Check if indices are within the range of the list length
    if 0 <= index1 < len(input_list) and 0 <= index2 < len(input_list):
        # Swap the elements at the specified indices
        input_list[index1], input_list[index2] = input_list[index2], input_list[index1]
        return True
    else:
        return False

# Take input from the user for the list elements (comma-separated)
try:
    user_input = input("Enter a list of elements (comma-separated): ")

    # Convert the user input to a list
    user_list = [int(item) if item.isdigit() else item for item in user_input.split(',')]

    # Take input from the user for the indices to swap
    index1 = int(input("Enter the first index to swap: "))
    index2 = int(input("Enter the second index to swap: "))

    # Call the function to swap elements
    success = swap_elements(user_list, index1, index2)

    # Display the result
    if success:
        print(f"\nList after swapping indices {index1} and {index2}:")
        print(user_list)
    else:
        print("Invalid indices. Please ensure indices are within the range of the list length.")

except ValueError:
    print("Invalid input. Please enter a valid list of elements and integer indices.")
