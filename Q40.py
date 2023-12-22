import random

def shuffle_list(input_list):
    # Use random.shuffle to shuffle the elements in-place
    random.shuffle(input_list)
    return input_list

# Take input from the user for the list elements (comma-separated)
try:
    user_input = input("Enter the list elements (comma-separated): ")

    # Convert the user input to a list
    user_list = [item.strip() for item in user_input.split(',')]

    # Call the function to shuffle the list
    shuffled_list = shuffle_list(user_list)

    # Display the shuffled list
    print(f"Original List: {user_list}")
    print(f"Shuffled List: {shuffled_list}")

except Exception as e:
    print(f"An error occurred: {e}")
