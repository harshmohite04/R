def merge_and_count_lines(file1_path, file2_path, merged_file_path):
    # Open the first file in read mode
    with open(file1_path, 'r') as file1:
        # Read the contents of the first file
        content1 = file1.read()

    # Open the second file in read mode
    with open(file2_path, 'r') as file2:
        # Read the contents of the second file
        content2 = file2.read()

    # Concatenate the contents of the two files
    merged_content = content1 + '\n' + content2

    # Write the merged content to the new file
    with open(merged_file_path, 'w') as merged_file:
        merged_file.write(merged_content)

    # Count the number of lines in the merged file
    with open(merged_file_path, 'r') as merged_file:
        line_count = sum(1 for line in merged_file)

    return line_count

# Example usage
file1_path = 'file1.txt'
file2_path = 'file2.txt'
merged_file_path = 'merged_file.txt'

lines_count = merge_and_count_lines(file1_path, file2_path, merged_file_path)

print(f'Merged file created at "{merged_file_path}"')
print(f'Number of lines in the merged file: {lines_count}')

