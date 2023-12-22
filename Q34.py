import string

def create_alphabet_file(file_path, letters_per_line):
    try:
        with open(file_path, 'w') as file:
            # Get all letters of the English alphabet
            alphabet = string.ascii_uppercase

            # Write the alphabet to the file with specified letters per line
            for i in range(0, len(alphabet), letters_per_line):
                line = alphabet[i:i + letters_per_line]
                file.write(line + '\n')

        print(f"File '{file_path}' created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Take input from the user for the file path and letters per line
file_path = input("Enter the file path to create: ")
letters_per_line = int(input("Enter the number of letters per line: "))

# Call the function to create the file
create_alphabet_file(file_path, letters_per_line)
\