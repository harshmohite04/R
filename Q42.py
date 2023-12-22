def count_vowels(input_string):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")

    # Use a list comprehension to count vowels in the string
    vowel_count = sum(1 for char in input_string if char in vowels)

    return vowel_count

# Take input from the user for the string
input_str = input("Enter a string: ")

# Call the function to count vowels
vowel_count_result = count_vowels(input_str)

# Display the result
print(f"Number of vowels in the string: {vowel_count_result}")
