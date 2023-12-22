# Open the text file in read mode
file_path = "file1.txt"  # Replace with the path to your text file
try:
    with open(file_path, 'r') as file:
        # Read each line from the file
        for line in file:
            # Print the line in reverse order
            reversed_line = line.strip()[::-1]
            print(reversed_line)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")


input_string = "Vishwakarma University"

# Extract substring from index 2 to 14
substring = input_string[2:15]

# Print the extracted substring
print(substring)
