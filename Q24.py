import re

def match_word_with_z(word):
    pattern = re.compile(r'\b\w*z\w*\b', re.IGNORECASE)
    return bool(re.match(pattern, word))

# Example usage:
word1 = "zebra"
word2 = "amazing"
word3 = "buzz"
word4 = "Zebra"

# Test the function
print(f"Does '{word1}' contain 'z'? {match_word_with_z(word1)}")
print(f"Does '{word2}' contain 'z'? {match_word_with_z(word2)}")
print(f"Does '{word3}' contain 'z'? {match_word_with_z(word3)}")
print(f"Does '{word4}' contain 'z'? {match_word_with_z(word4)}")



import re

def match_a_followed_by_bs(input_string):
    pattern = re.compile(r'a(b*)', re.IGNORECASE)
    match = re.search(pattern, input_string)
    return match.group(0) if match else None

# Example usage:
string1 = "ab"
string2 = "aaaabb"
string3 = "xyz"
string4 = "BBaBb"

# Test the function
print(f"Match in '{string1}': {match_a_followed_by_bs(string1)}")
print(f"Match in '{string2}': {match_a_followed_by_bs(string2)}")
print(f"Match in '{string3}': {match_a_followed_by_bs(string3)}")
print(f"Match in '{string4}': {match_a_followed_by_bs(string4)}")

