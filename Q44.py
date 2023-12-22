def copy_and_extract(file_path, copy_path, extract_path):
    try:
        # Copy the contents of the original file to the copy file
        with open(file_path, 'r') as original_file, open(copy_path, 'w') as copy_file:
            copy_file.write(original_file.read())

        # Extract the first two lines from the copied file
        with open(copy_path, 'r') as copied_file, open(extract_path, 'w') as extract_file:
            first_two_lines = [next(copied_file) for _ in range(2)]
            extract_file.writelines(first_two_lines)

        print("File copied successfully and first two lines extracted.")

    except FileNotFoundError:
        print("File not found. Please provide valid file paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
original_file_path = "original.txt"
copy_file_path = "copy.txt"
extracted_file_path = "extracted.txt"

copy_and_extract(original_file_path, copy_file_path, extracted_file_path)
