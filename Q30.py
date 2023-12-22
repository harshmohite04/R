# Function to search for literals in a string
def search_literals_in_string(search_string, literals):
    found_literals = [literal for literal in literals if literal in search_string]
    return found_literals

# Read the sample text from a file
try:
    with open("sample_text.txt", 'r') as file:
        sample_text = file.read()

    # Sample text
    print("Sample Text:")
    print(sample_text)

    # Searched words
    searched_words = ["fox", "dog", "horse"]

    # Search for literals in the sample text
    found_literals = search_literals_in_string(sample_text, searched_words)

    # Display the results
    print("\nSearched Words:")
    for word in searched_words:
        if word in found_literals:
            print(f"{word}: Found")
        else:
            print(f"{word}: Not Found")

except FileNotFoundError:
    print("File not found. Please make sure 'sample_text.txt' exists.")
except Exception as e:
    print(f"An error occurred: {e}")
