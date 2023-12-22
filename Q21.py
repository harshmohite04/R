def count_words(sentence):
    # Split the sentence into words using whitespace as the separator
    words = sentence.split()

    # Count the number of words
    num_words = len(words)

    return num_words

# Take input from the user for the sentence
user_sentence = input("Enter a sentence: ")

# Call the count_words function to count the number of words
number_of_words = count_words(user_sentence)

# Display the result
print(f"\nNumber of words in the sentence: {number_of_words}")
