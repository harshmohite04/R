def count_repeated_characters(input_string):
    char_count = {}

    # Count occurrences of each character
    for char in input_string:
        if char.isalpha():
            char = char.lower()  # Convert to lowercase to treat 'A' and 'a' as the same character
            char_count[char] = char_count.get(char, 0) + 1

    # Display characters with counts greater than 1
    for char, count in char_count.items():
        if count > 1:
            print(f"{char}  {count}")

# Sample String
sample_string = "thequickbrownfoxjumpsoverthelazydog"

# Call the function with the sample string
count_repeated_characters(sample_string)
