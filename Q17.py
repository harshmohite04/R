import re

def match_word_with_z(word):
    # Match a word containing 'z' not at the start or end
    pattern = re.compile(r'\b[^zZ]\w*z[^zZ]\b')
    return bool(re.match(pattern, word))

def match_valid_string(input_string):
    # Match a string containing only upper and lowercase letters, numbers, and underscores
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    return bool(re.match(pattern, input_string))

# Example usage:
word1 = "zebra"
word2 = "amazing"
word3 = "buzz"
word4 = "Zebra"
string1 = "Hello123"
string2 = "Valid_String_123"
string3 = "Invalid@String"

# Test the functions
print(f"Is '{word1}' matching? {match_word_with_z(word1)}")
print(f"Is '{word2}' matching? {match_word_with_z(word2)}")
print(f"Is '{word3}' matching? {match_word_with_z(word3)}")
print(f"Is '{word4}' matching? {match_word_with_z(word4)}")

print(f"\nIs '{string1}' matching? {match_valid_string(string1)}")
print(f"Is '{string2}' matching? {match_valid_string(string2)}")
print(f"Is '{string3}' matching? {match_valid_string(string3)}")
