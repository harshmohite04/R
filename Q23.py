def count_file_statistics(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            # Counting the number of characters
            num_characters = len(content)

            # Counting the number of words
            num_words = len(content.split())

            # Counting the number of spaces
            num_spaces = content.count(' ')

            # Counting the number of lines
            num_lines = content.count('\n') + 1  # Adding 1 to account for the last line

            return num_characters, num_words, num_spaces, num_lines

    except FileNotFoundError:
        return None

# Take input from the user for the file path
file_path = input("Enter the path of the file: ")

# Call the count_file_statistics function
result = count_file_statistics(file_path)

if result is not None:
    num_characters, num_words, num_spaces, num_lines = result

    # Display the results
    print(f"\nNumber of characters: {num_characters}")
    print(f"Number of words: {num_words}")
    print(f"Number of spaces: {num_spaces}")
    print(f"Number of lines: {num_lines}")
else:
    print("File not found. Please enter a valid file path.")
