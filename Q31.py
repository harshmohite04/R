def contains_all_alphabet_letters(input_string):
    # Convert the input string to lowercase to handle both upper and lowercase letters
    lowercase_string = input_string.lower()

    # Check if all letters from 'a' to 'z' are present in the string
    return all(letter in lowercase_string for letter in 'abcdefghijklmnopqrstuvwxyz')

# Take input from the user for the string
user_string = input("Enter a string: ")

# Check if the string contains all letters of the alphabet
result = contains_all_alphabet_letters(user_string)

# Display the result
if result:
    print("The string contains all letters of the alphabet.")
else:
    print("The string does not contain all letters of the alphabet.")
